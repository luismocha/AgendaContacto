from django import forms
from .models import Contacto
from django import forms
from django.contrib.auth import models
from django.db.models import fields
from django.forms.models import ModelForm
from .models import *

class Formulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields=["nombres", "apellidos","cedula","celular","email"]



class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ["id_contacto"]

