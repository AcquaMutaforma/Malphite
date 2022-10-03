from django.shortcuts import render
from Malphite.models import Settings
from .forms import SettingsForm
from .serializer import SettingsSerializer
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    settings = Settings.objects.all()
    return render(request, 'index.html', {'settings': settings, 'url': "/settings/edit/"+str(settings[0].id)})

#@api_view(['PUT'])
def EditAlarm(request, id):
    '''
    Updates the todo item with given todo_id if exists
    '''

    form = SettingsForm(request.POST)
    settings = Settings.objects.all()
    setting = Settings.objects.get(pk=id)
    #settings_serializer = SettingsSerializer(setting, data=(id, request.POST['Alarm']))
    print(form)
    print(form.is_valid())
    if form.is_valid():
        setting.Alarm = form.cleaned_data['Alarm']
        setting.save()
        return render(request, 'index.html', {'settings': settings, 'id': settings[0].id})
    return HttpResponse(status=201)

