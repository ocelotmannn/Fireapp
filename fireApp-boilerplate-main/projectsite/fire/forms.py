from django.forms import ModelForm
from django import forms
from .models import FireStation


class FireStationForm(ModelForm):
    class Meta:
        model = FireStation
        fields = "__all__"
