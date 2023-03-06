from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import redirect

from . import sveglia
from . import configManager as conf
from . import forms
from django.http import HttpResponse, JsonResponse
#from rest_framework import status

from .models import Risposta, Settings
from . import funzioni


def index(request):
    context = {'stato_sveglia': sveglia.STATO_SVEGLIA, 'orario_sveglia': sveglia.ORARIO_SVEGLIA,
               'user_id': conf.get_userId(), 'formOrario': forms.SvegliaForm(),
               'formUser': forms.UserForm()}
    return render(request, 'index.html', context)


""" 
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
"""


def risposte(request):
    """Pagina per visualizzare/aggiungere/rimuovere le risposte registrate dell'addetto """
    lista_risposte = Risposta.objects.all()
    context = {'lista_risposte': lista_risposte}
    return render(request, 'risposte.html', context)


def aggiungiRisposta(request):
    pass


def chiediElimina(request, idr):
    """Pagina per confermare la cancellazione della risposta registrata"""
    return render(request, 'chiediElimina.html', {'risposta': Risposta.objects.get(idr=idr)})


# Sul segnalibro "file upload django" c'è un esempio per correggere questa roba, nel caso non funziona
def eliminaConfermato(request, idr):
    funzioni.rimuovi_risposta(idr)
    return render(request, 'modifica_ok.html')


def attivaSveglia(request):
    sveglia.sveglia_attiva()
    return redirect('/Malphite/')


def spegniSveglia(request):
    sveglia.sveglia_spenta()
    return redirect('/Malphite/')


def modificaSveglia(request):
    if request.method == 'POST':
        form = forms.SvegliaForm(request.POST)
        if form.is_valid():
            sveglia.modificaSveglia(form.cleaned_data['Orario'])
            return render(request, 'modifica_ok.html')
    else:
        return index(request)


def modificaUserId(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            conf.set_userId(form.cleaned_data['User'])
            return render(request, 'modifica_ok.html')
    else:
        return index(request)
