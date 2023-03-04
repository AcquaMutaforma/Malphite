from django import forms

'''
In questo file ci sono i form che vengono caricati nella pagina html
'''


class SettingsForm(forms.Form):
    Alarm = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Alarm')


class SvegliaForm(forms.Form):
    Orario = forms.Textarea()


class UserForm(forms.Form):
    User = forms.Textarea()
