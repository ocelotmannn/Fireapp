from django.forms import ModelForm
from django import forms
from .models import FireStation, FireTruck, Firefighters


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
