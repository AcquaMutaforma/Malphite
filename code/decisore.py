"""Questo modulo si occupa di definire le azioni da prendere, in base
al comando ricevuto in formato {elementoTradotto}. Contiene una lista di
parole chiave associate ad un risposta, e una lista di appoggio per
valutare la risposta piu' corretta. """
import json
import esecutore
import elementoTradotto
import file_handler
import risposta


class Decisore:

    def __init__(self, esec: esecutore):
        self.mappa_logica = {}  # mappa con keywords -> id_risposta
        self.mappa_valutazione = {}  # mappa con obj_risposta -> N (punteggio per keywords corrispondenti alla risposta)
        self.esecutore = esec
        self.load_mappa()


    def valuta_comando(self, elem_trad: elementoTradotto.ElementoTradotto):
        f"""
    - controllo se e' presente una traduzione
    - con filtra_richiesta(elem_trad.traduzione) filtro la traduzione di {elem_trad} e ritorno una lista
    - per ogni parola nella lista, se e' presente nella {self.mappa_logica}, allora 
    incremento il valore nella {self.mappa_valutazione}
    - finita la lista, valuto la {self.mappa_valutazione}, se abbiamo un numero maggiore allora mando a esecutore,
    idem se abbiamo parita' o non trova riscontri nelle keywords
    - resetta mappa valutazione. 
    - infine, se non viene inviato al mess_handler elimina il file audio.
        """
        if(elem_trad.get_traduzione() == None):
            pass # todo: puo accadere di non avere traduzione? allora cosa faccio?
        dizionario_keywords = self.__filtra_richiesta(elem_trad.get_traduzione())
        for x in dizionario_keywords:
            id_risp = self.mappa_valutazione.get(x)
            tmp = self.mappa_valutazione.get(id_risp)
            self.mappa_valutazione.update(id_risp, tmp+1)
            # TODO correggere queste du cose, è troppo caldo

        # chiusura processo
        a = elem_trad.audio
        print(f"[Decisore] - Ho valutato il comando del file {a}")
        file_handler.elimina_audio(a)
        self.__reset_mappa_valutazione()
        pass  # todo

    def load_mappa(self):
        f"""Carica la mappa da un file, recuperato tramite fileHandler.
        Inizializza la {self.mappa_valutazione} con gli oggetti risposta, mentre inizializza
        la {self.mappa_logica} con le parole chiave relative alle risposte."""
        f = file_handler.get_mappa_decisore()
        lista = json.load(f)  # e' tipo <list> di oggetti <dict>
        for i in lista:
            risp = risposta.Risposta(i)
            for k in risp.keywords:
                if k is None:
                    continue
                self.mappa_logica[str(k).lower()] = str(risp.idr)
                # se e' gia presente una keyword? modifichiamo il valore (id) in una lista di id (?)idk
            self.mappa_valutazione[risp.idr] = 0

    def add_risposta(self):
        """Aggiunge una nuova risposta alla tabella, e richiede a fileHandler
        di modificare il file della mappa."""
        pass  # todo

    def rm_risposta(self):
        """Se presente, rimuove una nuova risposta dalla tabella, e richiede a fileHandler
            di modificare il file della mappa."""
        pass  # todo

    def __reset_mappa_valutazione(self):
        for x in self.mappa_valutazione.keys():
            self.mappa_valutazione[x] = 0

    def __filtra_richiesta(self, tmp_s: str):
        """Metodo che sottrae le parole piu' corte di 3 caratteri e ritorna una lista
                con le parole presenti nel comando ricevuto"""
        return {}
