import registratore as rg
import logManager as log
import numpy as np
import output_handler as out
import file_handler as fh
import asyncio

try:
    import botTelegram
except Exception as e:
    log.logError(f"BotTelegram non avviato - {e}")

# django
import risposteHandler as rh

# spech to text
import stt
import csv_creator
import os

# Per comodità
ATTIVA = True
PASSIVA = False


def main(MODALITA=PASSIVA):
    try:
        if MODALITA:
            try:
                modello = stt.Model("STT_MODEL_ITA/model.tflite")
                modello.enableExternalScorer("STT_MODEL_ITA/ita_scorer.scorer")
                modAttiva(model=modello)
            except RuntimeError as e:
                log.logCritical(f'{e} - STT Model ')
                exit(1)
        else:
            modPassiva()
    except KeyboardInterrupt:
        print("Addio e grazie per il pesce :')")
        exit(0)


def modPassiva():
    """Funzione di appoggio per il training, registra file audio e inserisce i dati nel file CSV"""
    registratore = rg.get_audio_stream()
    registratore.start()
    log.logDebug("Inzio registrazione MOD ATTIVA")
    print("Inserisci la frase che dirai e premi invio> ")
    frase = input()
    while True:
        print("Premi un tasto per registrare, per uscire usa CTRL + C")
        input()  # se preme CTRL + C, il try-catch del main() termina l'esecuzione
        print("recording..")
        audio_filename = fh.audio_to_file(rg.frequency, __get_registrazione(registratore=registratore))
        log.logInfo("salvataggio file { " + audio_filename + " }")
        csv_creator.addLineToCSV(audio_filename, os.path.getsize(audio_filename), frase)
        print("done!")
        # break  # per un solo ciclo


def modAttiva(model):
    """Funzione principale, ascolta l'input, se non è vuoto procede a blocchi di 3 secondi (modificabile in
    registratore.py). Una volta sommati 3 blocchi o dopo aver trovato un blocco con solo rumore, si traduce con IA,
    se trova riscontro ok, sennò salva l'input come file audio e invia tramite telegram quello che non ha compreso.

    Update:
    Aggiunto un secondo tentativo di comprensione della frase."""
    registratore = rg.get_audio_stream()
    registratore.start()
    log.logDebug("Inzio registrazione MOD ATTIVA")
    secondo_tentativo = True  # True = disponibile, False = gia' garantito
    while True:
        riproduzioneProattiva()
        temporaneo = __get_registrazione(registratore=registratore)
        frase = model.stt(np.frombuffer(temporaneo, dtype=np.int16))
        print(f"Frase compresa = [ {frase} ]")
        # se non trovo una risposta, creo il file audio con il buffer temporaneo, lo invio insieme
        # alla traduzione all'addetto con il bot telegram
        log.logDebug(f"La frase compresa dal model è: {frase}")
        if __decidere(frase):
            if secondo_tentativo:
                out.nonCapitoRipeti()
                secondo_tentativo = False
                continue
            else:
                secondo_tentativo = True
            nome_file = fh.audio_to_file(rg.frequency, temporaneo)
            try:
                asyncio.run(botTelegram.invia_audio(nome_file, frase))
                log.logInfo("\nRisposta non trovata. Domanda compresa = [" + frase + "]. File = [" +
                            nome_file + "]")
            except Exception:
                log.logError("\nInvio del file non compreso fallito")

        # break  # per un solo ciclo


def __get_registrazione(registratore, numero_secondi=3):
    """Registra a blocchi da 3 secondi, se trova suoni con decibel alti (vedi registratore.py) allora li salva nel
    buffer, il loop continua per 3 blocchi ( 3 * 3 = 9 sec max) oppure se il blocco successivo non contiene suoni
    degni di nota (sopra i decibel, vedi registratore.py).
    :return array numpy con formato np.16, compatibile con coquiAI"""
    log.logDebug("avvio funzione __get_registrazione")
    max_giri_a_vuoto = 1
    contatore_giri_a_vuoto = 0
    buffer = np.zeros(shape=(1, 1), dtype=np.int16)
    contatore_buffer = 0
    max_giri = 2  # ovvero al massimo sono 6 secondi di audio (numero_secondi * max_giri+1)
    while True:
        solo_rumore = True
        tmp, _ = registratore.read(rg.frequency * numero_secondi)
        """# Utile per il debug - inserisce nel file log i valori registrati
        massimo_valore = 0
        minimo_valore = 0"""
        for x in tmp.tolist():  # ogni elemento e' una lista con (value, channel) quindi ([0],[1]), ([0],[1]) etc..
            valore = x[0]
            if abs(valore) > rg.soglia_y:
                solo_rumore = False
        """if valore > massimo_valore:
                massimo_valore = valore
            if valore < minimo_valore:
                minimo_valore = valore
        log.logDebug("massimo = " + str(massimo_valore))
        log.logDebug("minimo = " + str(minimo_valore))"""

        if solo_rumore:
            contatore_giri_a_vuoto += 1
            log.logDebug('blocco "vuoto", contatore_giri_a_vuoto++')
            print('X')
        else:
            if contatore_buffer == 0:
                buffer = tmp
            else:
                buffer = np.concatenate((buffer, tmp), dtype=np.int16)
            log.logDebug('buffer non vuoto, concatenazione completata')
            contatore_buffer += 1
            contatore_giri_a_vuoto = 0
            print(str(contatore_buffer))
        if (contatore_giri_a_vuoto >= max_giri_a_vuoto and contatore_buffer > 0) or contatore_buffer > max_giri:
            log.logDebug('blocchi audio minori della soglia rumore = ' + str(contatore_giri_a_vuoto) +
                         ' contatore blocchi buffer = ' + str(contatore_buffer))
            return buffer


def __decidere(frase: str):
    """
    Algoritmo di scelta basato sulla valutazione delle parole comprese dal Speech-to-Text.
    Per ogni parola più lunga di 3 caratteri, controllo la presenza nel DB locale e salvo gli ID delle risposte
    corrispondenti. Ogni risposta guadagna un punto per ogni parola chiave che ha in comune con la frase compresa,
    se si trova una risposta con punteggio più alto e unico (non uguale ad un'altra risposta) allora viene riprodotto
    il relativo audio.
    :return: False, caso in cui ho trovato e riprodotto l'audio risposta, True, serve mandare un messaggio all'operatore
    """
    # creo un array con gli ID delle risposte e il numero di volte che vengono trovati
    lista_valutazione = {}
    parole_chiave = str.split(frase, ' ')

    for x in parole_chiave:
        if len(x) < 3:
            continue
        key = rh.get_idrisposte_con_keyword(x)  # Richiesta al db locale
        if key is None:
            continue
        if key in lista_valutazione.keys():
            lista_valutazione[key] = lista_valutazione.get(key) + 1
        else:
            lista_valutazione[key[0]] = 1
    # cerco l'id che compare piu volte
    idRisposta = 0
    massimo = 0
    unico = True
    for k, v in lista_valutazione.items():
        if massimo < v:
            idRisposta = k
            massimo = v
            unico = True
        elif massimo == v:
            unico = False

    # Se ho trovato una risposta (il suo id) che compare una sola volta allora abbiamo una risposta, altrimenti
    # e' possibile che ci siano piu risposte valide o nessuna, non sapendo quale sia quella corretta mandiamo tutto
    # all'operatore tramite telegram
    if unico and (idRisposta != 0) and idRisposta is not None:
        # Riproduco audio risposta
        risposta = rh.get_risposta_by_idr(idrisposta=idRisposta)
        out.riproduci_audio('mysite/' + str(risposta[2]))
        #  2 = percorso file, 1 = nome file
        return False  # Non serve mandare un messaggio telegram
    else:
        # Non ho trovato la risposta =( -> serve un messaggio telegram
        return True


def riproduzioneProattiva():
    """Tenta di riprodurre l'audio ricevuto da telegram per poi eliminarlo."""
    try:
        out.riproduci_audio('ricevutiTelegram/temporaneo.wav')
        fh.elimina_audio('ricevutiTelegram/temporaneo.wav')
    except Exception:
        return


main(ATTIVA)
