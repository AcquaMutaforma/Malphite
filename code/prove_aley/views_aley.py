from django.shortcuts import render
from models_aley import Risposta, Keyword
from forms_ale import SettingsForm
from django.http import HttpResponse, JsonResponse
from django.template import loader
import risposte_handler


def index(request):
    pass


def risposte(request):
    lista_risposte = Risposta.objects.all()
    context = {'lista_risposte': lista_risposte}
    return render(request, 'Malphite/risposte.html', context)


def elimina(request, idr):
    risposte_handler.rimuovi_risposta(idr)
    return risposte(request)


def chiediElimina(request, idr):
    return render(request, 'Malphite/chiedi-elimina.html', {'risposta': risposte_handler.get_risposta_by_idr(idr)})
