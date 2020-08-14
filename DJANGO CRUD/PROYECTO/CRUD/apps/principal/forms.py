from django import forms
from .models import Persona,Ciudad,TipoDocumento
from django.forms import ModelChoiceField



class Personaform(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('__all__') # tambien con una tupla, ejemplo: ('nombre','apellido')