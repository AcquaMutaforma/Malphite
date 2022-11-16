import registratore as rg
import traduttore
import logManager as log
import file_handler as fh
import numpy as np
import output_handler as out
import message_handler
# django imports
import risposte_handler as rh


ATTIVA = True
PASSIVA = False


def main(MODALITA=PASSIVA):
    # Manca tutta la parte della configurazione, i dati sono nel blocco note sul desktop
    # in Malphite/mysite/settings c'è una configurazione del database, ip, port, username, pass da usare come esempio
    if MODALITA:
        modAttiva("model_path")  # todo: aggiungere config.modelPath
    else:
        modPassiva()
    """
    registratore = rg.get_audio_stream()
    while True:
        temporaneo = __get_registrazione(registratore=registratore)
        if MODALITA == ATTIVA:
            frase = traduttore.traduci(temporaneo)
            risultato = __decidere(frase)
            # se non trovo una risposta, invio audio e traduzione ad addetto con telegram
            if not risultato:
                nome_file = fh.audio_to_file(rg.frequency, temporaneo)
                message_handler.invia_richiesta(nome_file, frase)
                log.logInfo("\nRisposta non trovata. Domanda = [" + frase + "]. File = [" +
                            nome_file + "]")
        else:
            audio_filename = fh.audio_to_file(rg.frequency, temporaneo)
            log.logInfo("salvataggio file { " + audio_filename + " }")
            # Verione server remoto
            # connessioneManager.invia(audio_filename)
            # fh.elimina_audio(audio_filename)
            """


def modPassiva():
    registratore = rg.get_audio_stream()
    while True:
        audio_filename = fh.audio_to_file(rg.frequency, __get_registrazione(registratore=registratore))
        log.logInfo("salvataggio file { " + audio_filename + " }")


def modAttiva(model_path: str):
    registratore = rg.get_audio_stream()
    traduttore.setModel(model_path)
    while True:
        temporaneo = __get_registrazione(registratore=registratore)
        frase = traduttore.traduci(temporaneo)
        risultato = __decidere(frase)
        # se non trovo una risposta, invio audio e traduzione all'addetto con telegram
        if not risultato:
            nome_file = fh.audio_to_file(rg.frequency, temporaneo)
            message_handler.invia_richiesta(nome_file, frase)
            log.logInfo("\nRisposta non trovata. Domanda = [" + frase + "]. File = [" +
                        nome_file + "]")


def __get_registrazione(registratore, numero_secondi=3):
    giri_a_vuoto = 1
    contatore_giri_a_vuoto = 0
    buffer = np.ndarray
    contatore_buffer = 0
    while True:
        solo_rumore = True
        tmp = registratore.read(rg.frequency * numero_secondi)

        for x in np.nditer(tmp):
            if abs(x) > rg.soglia_y:
                solo_rumore = False
                break
        # se ogni elemento è < di 0.003 allora ignoro il nuovo blocco, scrivo e invio un file audio
        if solo_rumore:
            contatore_giri_a_vuoto += 1
            log.logInfo('contatore giri a vuoto ++')
        else:
            buffer = np.concatenate(buffer, tmp)
            contatore_buffer += 1
            contatore_giri_a_vuoto = 0

        # todo: dovrebbe restituire solo se l'ultimo blocco era silenzioso, lo fa? controlla !
        if contatore_giri_a_vuoto >= giri_a_vuoto and contatore_buffer > 0:
            return buffer


def __decidere(frase: str):
    # creo un array con gli ID delle risposte e il numero di volte che vengono trovati
    lista_valutazione = {}
    parole_chiave = str.split(frase, ' ')

    for x in parole_chiave:
        key = rh.get_idrisposte_con_keyword(x)  # Richiesta al db locale
        if key in lista_valutazione.keys():
            lista_valutazione[key] = lista_valutazione.get(key) + 1
        else:
            lista_valutazione[key] = 1
    # cerco l'id che compare piu volte
    idRisposta = 0
    massimo = 0
    unico = True
    for k, v in lista_valutazione.items():
        if massimo < v:
            idRisposta = k
            massimo = v
            unico = True
        if massimo == v:
            unico = False

    # Se ho trovato una risposta (il suo id) che compare una sola volta allora abbiamo una risposta, altrimenti
    # e' possibile che ci siano piu risposte valide o nessuna, non sapendo quale sia quella corretta mandiamo tutto
    # all'operatore tramite telegram
    if unico and (idRisposta != 0):
        out.riproduci_audio(rh.get_risposta_by_idr(idrisposta=idRisposta).percorsoFile)
        return True
    else:
        return False

