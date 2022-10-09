from django.forms import model_to_dict
from django.shortcuts import render
from Malphite.models import Settings
from .forms import SettingsForm
from .serializer import SettingsSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# Create your views here.

def index(request, id):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SettingsForm(request.POST)
        settings = Settings.objects.all()
        setting = Settings.objects.get(pk=id)
        # check whether it's valid:
        if form.is_valid():
            setting.Alarm = form.cleaned_data['Alarm']
            setting.save()
            return render(request, 'index.html', {'form': form ,'url': "/settings/" + str(settings[0].id)})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SettingsForm()
        try:
            setting = Settings.objects.get(pk=id)
            form = SettingsForm(initial=model_to_dict(setting))
        except Settings.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return render(request, 'index.html', {'form': form,'url': "/settings/" + str(setting.id)})

