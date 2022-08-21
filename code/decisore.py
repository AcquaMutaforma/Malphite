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

    def __init__(self, esec: esecutore.Esecutore):
        self.mappa_logica = {}  # mappa con keyword -> id_risposta
        self.mappa_valutazione = {}  # mappa con id_risposta -> punteggio (per keywords corrispondenti alla risposta)
        self.mappa_risposte = {}  # mappa con id_risposta -> dict:risposta
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
        if elem_trad.get_traduzione() is None:
            return  # todo: puo succedere di non avere traduzione? allora cosa faccio?
        lista_keywords = self.__filtra_richiesta(elem_trad.get_traduzione())
        for keyword in lista_keywords:
            id_risp = self.mappa_logica.get(keyword)
            if id_risp is None:
                continue  # se non e' presente la keyword passo alla prossima
            self.mappa_valutazione[id_risp] = (self.mappa_valutazione.get(id_risp) + 1)
        massimo = 0
        doppio = False
        for key in self.mappa_valutazione.keys():
            tmp = self.mappa_valutazione.get(key)
            if tmp > massimo:
                massimo = tmp
                doppio = False
            elif tmp == massimo:
                doppio = True
        if massimo == 0 or doppio is True:
            self.esecutore.richiesta_non_gestita(elem_trad)
        else:
            self.esecutore.esegui_operazione(self.mappa_risposte.get(id_risp).get("registrazione"))
            # file_handler.elimina_audio(elem_trad.get_audio()) todo quando eliminiamo il file? qua puo essere rischioso
        # chiusura processo ------------------
        self.__reset_mappa_valutazione()
        print(f"[Decisore] - Ho valutato il comando del file {elem_trad.get_audio()}")

    def load_mappa(self):
        f"""Carica la mappa da un file, recuperato tramite fileHandler.
        Inizializza la {self.mappa_valutazione} con gli oggetti risposta, mentre inizializza
        la {self.mappa_logica} con le parole chiave relative alle risposte."""
        f = file_handler.get_mappa_decisore()
        lista = json.load(f)  # e' tipo <list> di oggetti <dict>
        f.close()
        for i in lista:
            risp = risposta.Risposta(i)
            if risp is None:
                continue
            for k in risp.keywords:
                self.mappa_logica[str(k).lower()] = str(risp.idr)
                # se e' gia presente una keyword? modifichiamo il valore (id) in una lista di id (?)idk
            self.mappa_valutazione[risp.idr] = 0
            self.mappa_risposte[risp.idr] = risp

    def add_risposta(self, nuova_risposta: dict):
        """Aggiunge una nuova risposta alla tabella valutazione e le sue risposte alla tabella logica.
        richiede a fileHandler di modificare il file della mappa."""
        temp = risposta.Risposta(nuova_risposta)
        if temp is None:
            return False  # todo: cosa fa se l'input non e' corretto?
        for key in temp.keywords:
            self.mappa_logica[key] = temp.idr
        self.mappa_valutazione[temp.idr] = 0
        self.mappa_risposte[temp.idr] = temp
        self.__aggiorna_mappa()
        return True

    def rm_risposta(self, idr: int):
        """Se presente, rimuove una nuova risposta dalla tabella, e richiede a fileHandler
            di modificare il file della mappa."""
        temp = self.mappa_risposte.get(idr)
        self.mappa_valutazione.pop(idr)
        for x in temp.get("keywords"):
            self.mappa_logica.pop(x)
        self.mappa_risposte.pop(idr)
        self.__aggiorna_mappa()

    def __reset_mappa_valutazione(self):
        for x in self.mappa_valutazione.keys():
            self.mappa_valutazione[x] = 0

    def __filtra_richiesta(self, testo: str):
        """Metodo che sottrae le parole piu' corte di 3 caratteri e ritorna una lista
        con le parole presenti nel comando ricevuto"""
        tmp = testo.lower().split()
        for x in tmp:
            if x.__len__() <= 3:
                tmp.remove(x)
        return tmp

    def __aggiorna_mappa(self):
        """Metodo che prende tutti gli obj risposta, li trasforma in una lista di str json e manda
        il tutto al file-handler"""
        lista = self.mappa_risposte.values()
        toreturn = []
        for x in lista:
            toreturn.append(x.getjson())
        file_handler.update_file_mappa(toreturn)
