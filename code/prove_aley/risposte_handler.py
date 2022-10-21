from models_aley import Risposta, Keyword


def __aggiungi_risposta_alla_keyword(keyword: str, idRisposta: int):
    lista_oggetti_keyword = Keyword.objects.filter(keyword=keyword)  # il formato e' dictionary
    if len(lista_oggetti_keyword) < 1:
        parola = Keyword.objects.create(keyword=keyword, idRisposta=idRisposta)
        parola.save()
    else:
        for x in lista_oggetti_keyword:
            x.self.idRisposta.append(idRisposta)
            x.save()


def __flush_keyword_senza_risposte():
    lista = Keyword.objects.all()
    for x in lista:
        if len(x.idRisposta) == 0:
            x.remove()


def get_risposta_by_idr(idrisposta: int) -> Risposta:
    return Risposta.objects.get(idr=idrisposta)


def get_idrisposte_con_keyword(keyword: str) -> tuple[str]:
    return Keyword.objects.values_list('idRisposta')


def aggiungi_risposta(nome: str, percorsoFile: str, keywords: ()):
    toAdd = Risposta.objects.create(nome=nome, percorsoFile=percorsoFile)
    toAdd.save()
    for x in keywords:
        __aggiungi_risposta_alla_keyword(keyword=x, idRisposta=toAdd.idr)


def rimuovi_risposta(idRisposta: int):
    toRemove = Risposta.objects.get(idr=idRisposta)
    toRemove.remove()
    __flush_keyword_senza_risposte()
