from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import redirect

from . import sveglia
from . import configManager as conf
from . import forms
from django.http import HttpResponse, JsonResponse
#from rest_framework import status

from .models import Risposta, Relazione, Keyword
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
    if request.method == 'POST':
        form = forms.RispostaForm(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['Nome']
            path = gestioneFileCaricato(request.FILES['FileAudio'], nome)
            funzioni.aggiungi_risposta(nome, path, form.cleaned_data['Keywords'])
            return render(request, 'modifica_ok.html')
        else:
            return render(request, 'invalid.html')
    else:
        return render(request, 'aggiungiRisposta.html', {'form': forms.RispostaForm})


def gestioneFileCaricato(f, nome: str):
    try:
        percorso = 'risposteRegistrate/' + nome + ".wav"
        with open(percorso, 'wb+') as destinazione:
            for chunk in f.chunks():
                destinazione.write(chunk)
        return percorso
    except PermissionError:
        pass


def chiediElimina(request, idr):
    """Pagina per confermare la cancellazione della risposta registrata"""
    risposta = Risposta.objects.get(idr=idr)
    tutte = Relazione.objects.filter(idRisposta=risposta.idr)
    lista = []
    for x in tutte:
        tmp = x.idKeyword
        lista.append(Keyword.objects.get(id=tmp.id).__str__)
    return render(request, 'chiediElimina.html', {'risposta': risposta,
                                                  'lista_keywords': lista})


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
