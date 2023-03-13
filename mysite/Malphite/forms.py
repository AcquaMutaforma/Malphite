from django import forms

'''
In questo file ci sono i form che vengono caricati nella pagina html
'''

"""
class SettingsForm(forms.Form):
    Alarm = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Alarm')
"""


class SvegliaForm(forms.Form):
    Orario = forms.CharField(label='Orario', max_length=10)


class UserForm(forms.Form):
    User = forms.CharField(label='User', max_length=15)


class RispostaForm(forms.Form):
    Nome = forms.CharField(label='Nome', max_length=150)
    FileAudio = forms.FileField(error_messages={'required': 'inserire il file :<'})
    Keywords = forms.CharField(label='Keywords', max_length=150)
