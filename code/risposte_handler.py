import risposta_model


def aggiungi_risposta(nome: str, percorsoFile: str, keywords: ()):
    toAdd = risposta_model.Risposta.objects.create(nome=nome, percorsoFile=percorsoFile)
    toAdd.save()
    for x in keywords:
        risposta_model.aggiungi_risposta_alla_keyword(keyword=x, idRisposta=toAdd.idr)


def rimuovi_risposta(idRisposta: int):
    toRemove = risposta_model.Risposta.objects.get(idr=idRisposta)
    toRemove.remove()
    risposta_model.flush_keyword_senza_risposte()
