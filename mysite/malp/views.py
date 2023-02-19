from django.forms import model_to_dict
from django.shortcuts import render
from models import Settings
from .forms import SettingsForm
from django.http import HttpResponse, JsonResponse
from rest_framework import status

import risposte_handler
from models import Risposta


def index(request):
    pass


def alarm(request, id):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SettingsForm(request.POST)
        setting = Settings.objects.get(pk=id)
        # check whether it's valid:
        if form.is_valid():
            setting.Alarm = form.cleaned_data['Alarm']
            setting.save()
            return render(request, 'index.html', {'form': form, 'url': "/settings/" + str(setting.id)})
    # if a GET (or any other method) we'll create a blank form
    else:
        try:
            setting = Settings.objects.get(pk=id)
            form = SettingsForm(initial=model_to_dict(setting))
        except Settings.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return render(request, 'index.html', {'form': form, 'url': "/settings/" + str(setting.id)})


def risposte(request):
    lista_risposte = Risposta.objects.all()
    context = {'lista_risposte': lista_risposte}
    return render(request, 'Malphite/risposte.html', context)


def elimina(request, idr):
    risposte_handler.rimuovi_risposta(idr)
    return risposte(request)


def chiediElimina(request, idr):
    return render(request, 'Malphite/chiedi-elimina.html', {'risposta': risposte_handler.get_risposta_by_idr(idr)})
