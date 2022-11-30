import registratore as rg
import traduttore
import logManager as log
import file_handler as fh
import numpy as np
import output_handler as out
import message_handler
# django
import risposte_handler as rh


ATTIVA = True
PASSIVA = False


def main(MODALITA=PASSIVA):
    # Manca tutta la parte della configurazione, i dati sono nel blocco note sul desktop
    if MODALITA:
        modAttiva()
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
    registratore.start()
    fh.cartella_registrazioni = 'test_passiva/'
    while True:
        try:
            print("recording..")
            audio_filename = fh.audio_to_file(rg.frequency, __get_registrazione(registratore=registratore))
            log.logInfo("salvataggio file { " + audio_filename + " }")
            print("done!")
        except KeyboardInterrupt:
            print("Addio e grazie per il pesce :')")
            exit(0)
        # break  # per un solo ciclo


def modAttiva():
    registratore = rg.get_audio_stream()
    registratore.start()
    while True:
        try:
            temporaneo = __get_registrazione(registratore=registratore)
            frase = traduttore.traduci(temporaneo)
            risultato = __decidere(frase)
            # se non trovo una risposta, invio audio e traduzione all'addetto con telegram
            if not risultato:
                nome_file = fh.audio_to_file(rg.frequency, temporaneo)
                message_handler.invia_richiesta(nome_file, frase)
                log.logInfo("\nRisposta non trovata. Domanda = [" + frase + "]. File = [" +
                            nome_file + "]")
        except KeyboardInterrupt:
            print("Addio e grazie per il pesce :')")
            exit(0)


def __get_registrazione(registratore, numero_secondi=3):
    log.logDebug("avvio funzione __get_registrazione")
    giri_a_vuoto = 1
    contatore_giri_a_vuoto = 0
    buffer = np.empty(shape=(1, 1))
    contatore_buffer = 0
    max_giri = 2
    while True:
        massimo_valore = 0
        minimo_valore = 0
        solo_rumore = True
        tmp, _ = registratore.read(rg.frequency * numero_secondi)  # shape(1,1) una colonna per canale (sample,chann)

        for x in tmp.tolist():  # ogni elemento e' una lista con (value, channel) quindi ([0],[1]), ([0],[1]) etc..
            valore = x[0]
            if abs(valore) > rg.soglia_y:
                solo_rumore = False
            if valore > massimo_valore:
                massimo_valore = valore
            if valore < minimo_valore:
                minimo_valore = valore
        log.logDebug("massimo = " + str(massimo_valore))
        log.logDebug("minimo = " + str(minimo_valore))

        if solo_rumore:
            contatore_giri_a_vuoto += 1
            log.logDebug('blocco "vuoto", contatore_giri_a_vuoto++')
        else:
            if contatore_buffer == 0:
                buffer = tmp
            else:
                buffer = np.concatenate((buffer, tmp))
            log.logDebug('buffer non vuoto, concatenazione completata')
            contatore_buffer += 1
            contatore_giri_a_vuoto = 0

        if (contatore_giri_a_vuoto >= giri_a_vuoto and contatore_buffer > 0) or contatore_buffer > max_giri:
            log.logDebug('blocchi audio di vuoto = ' + str(contatore_giri_a_vuoto) +
                         ' contatore buffer = ' + str(contatore_buffer))
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


main()
