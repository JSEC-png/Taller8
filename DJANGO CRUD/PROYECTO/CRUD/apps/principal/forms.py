from django import forms
from .models import Persona,Ciudad,TipoDocumento
from django.forms import ModelChoiceField


class Dateinput(forms.DateInput):
    input_type = 'date'

class Personaform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    fechaNacimiento  = forms.CharField(widget= Dateinput)
    
    class Meta:
        model = Persona
        fields = ('__all__') # tambien con una tupla, ejemplo: ('nombre','apellido')
        