from django import forms
from myapp.models import HistoryWeather


class WeatherForm(forms.Form):
    class Meta:
        model = HistoryWeather
    location = forms.ChoiceField(choices=HistoryWeather.LOCATION)
    humidity = forms.CharField(label='Humedad')
    temperature = forms.CharField(label='Temperature')
