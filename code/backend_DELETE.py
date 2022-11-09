"""Si puo' personalizzare il programma modificando i seguenti oggetti:
myapi, registratore, message_handler e output_handler"""
import json

import servizio_AssemblyAI as MyAPI
import elementoTradotto
import registratore
import file_handler as fh
import risposta_model
import output_handler
import events_handler


def suona_sveglia():
    output_handler.riproduci_audio("sveglia.mp3")


def __traduci(audio: str) -> elementoTradotto.ElementoTradotto or None:
    """ Metodo che attraverso l'oggetto api che contiene, traduce un audio in testo """
    print("[Traduttore] - avvio API")
    testo = MyAPI.traduzione(audio)
    print(f"[Traduttore] - traduzione= {testo}")
    if testo is not None:
        return elementoTradotto.ElementoTradotto(file_audio=audio, trad=testo)
    else:
        print("[Traduttore] - traduzione non riuscita, testo = None")
        return None


def __filtra_richiesta(testo: str):
    """Metodo che sottrae le parole piu' corte di 3 caratteri e ritorna una lista
    con le parole presenti nel comando ricevuto"""
    tmp = testo.lower().split()
    for x in tmp:
        if len(x) <= 3:
            tmp.remove(x)
    return tmp


def start():
    # ------ Avvio oggetti necessari ------
    # mess_h = message_handler.TeleBot()

    # ------ Non avevo altre idee, quindi per ora si avvia cosi' ------------------------
    print("Scrivi 'start' per iniziare, altrimenti chiudo")
    comando = input()
    if 'start' not in comando:
        exit(0)

    registrazione = registratore.get_audio(secondi=3.0)
    elem_tradotto = __traduci(registrazione)

    testo_filtrato = __filtra_richiesta(elem_tradotto.traduzione)
    lista_valutazione = {}
    # creo un array con gli ID delle risposte e il numero di volte che vengono trovati
    for x in testo_filtrato:
        key = risposta_model.get_idrisposte_con_keyword(x)
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
    # e' possibile che ci siano piu risposte valide, non sapendo quale sia quella corretta mandiamo tutto
    # all'operatore tramite telegram
    if unico and (idRisposta != 0):
        output_handler.riproduci_audio(risposta_model.get_risposta_by_idr(idrisposta=idRisposta).percorsoFile)
    else:
        print("\nRisposta non trovata. Domanda = '" + elem_tradotto.traduzione + "'\n")
        # message_handler.invia_richiesta(elem_tradotto)

    print("Ok - i'm done")
    exit(0)


def __aggiorna_config(config: dict):
    fh.scrivi_config(config)


def imposta_sveglia(orario: str):
    events_handler.EVENTO_SVEGLIA = events_handler.crea_schedule(orario=orario)
    events_handler.STATO_SVEGLIA = True


def modifica_stato_sveglia(stato: bool):
    events_handler.STATO_SVEGLIA = stato


def main():
    configurazione = fh.leggi_config()
    imposta_sveglia(orario=configurazione['orario_sveglia'])
    modifica_stato_sveglia(stato=configurazione['stato_sveglia'])
    while True:
        # analizza audio e registra se serve
        pass


start()
