from django import forms

class SettingsForm(forms.Form):
    Alarm = forms.TimeField(label='Alarm')