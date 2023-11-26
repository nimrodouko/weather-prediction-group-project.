# forms.py
from django import forms
from .models import WeatherData

class WeatherForm(forms.ModelForm):
    class Meta:
        model = WeatherData
        fields = ['temperature', 'humidity', 'wind','soil','terrain']

    

        

        
