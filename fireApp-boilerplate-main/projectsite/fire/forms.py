from django.forms import ModelForm
from django import forms
from .models import FireStation, FireTruck, Firefighters, Incident, Locations, WeatherConditions


class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
    
class FireTruckForm(ModelForm):
    class Meta:
        model = FireTruck
        fields = "__all__"

class FireFighterForm(ModelForm):
    class Meta:
        model = Firefighters
        fields = "__all__"

class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = "__all__"

class LocationForm(ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"

class WeatherConditionForm(ModelForm):
    class Meta:
        model = WeatherConditions
        fields = "__all__"
