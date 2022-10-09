from django import forms

class SettingsForm(forms.Form):
    Alarm = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label='Alarm')