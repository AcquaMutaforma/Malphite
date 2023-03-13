"""
Funzioni che vengono chiamate nelle pagine web generate per alterare i dati presenti nel database
"""
from .models import Risposta, Keyword, Relazione
from . import logManager as log
from . import file_handler as fh


def __aggiungi_risposta_alla_keyword(keyword: str, risp: Risposta):
    """Spezzo la stringa keyword e provo ad inserirle una per una,
        controllando che non siano già presenti. In entrambi i casi inserisco
        una nuova relazione con idRisposta e id della keyword"""
    lista = keyword.split()
    for x in lista:
        try:
            tmp = Keyword.objects.get(keyword=x)
            __aggiungiRelazione(risposta=risp, keyword=tmp)
        except Keyword.DoesNotExist:
            newKeyw = Keyword.objects.create(keyword=x)
            newKeyw.save()
            __aggiungiRelazione(risposta=risp, keyword=newKeyw)
        except Exception as e:
            log.logError(f"Inserimento keyword fallito - {e}")


def __flush_keyword_senza_risposte():
    lista = Keyword.objects.all()
    for x in lista:
        try:
            Relazione.objects.get(idKeyword=x.id)
        except Relazione.DoesNotExist:
            x.delete()
        except Exception as e:
            log.logError(f"Flush di keyword senza risposte collegate FALLITO - {e}")


def aggiungi_risposta(nome: str, percorsoFile: str, keywords: str):
    toAdd = Risposta.objects.create(nome=nome, percorsoFile=percorsoFile)
    toAdd.save()
    log.logDebug(f"aggiunta risposta {nome} - {percorsoFile}")
    __aggiungi_risposta_alla_keyword(keyword=keywords, risp=toAdd)


def rimuovi_risposta(idRisposta: int):
    try:
        toRemove = Risposta.objects.get(idr=idRisposta)
        toRemove.delete()
        fh.elimina_audio(toRemove.percorsoFile)
        __flush_keyword_senza_risposte()
    except Risposta.DoesNotExist:
        log.logError(f"IDRisposta {idRisposta} non esiste, non posso cancellarlo")


def __aggiungiRelazione(risposta, keyword):
    newRelaz = Relazione.objects.create(idRisposta=risposta, idKeyword=keyword)
    newRelaz.save()
