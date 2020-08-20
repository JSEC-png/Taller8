from django import forms
from .models import Persona,Ciudad,TipoDocumento
from django.forms import ModelChoiceField


class Dateinput(forms.DateInput):
    input_type = 'date'

class Personaform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'id':'pass'}))
    fechaNacimiento  = forms.CharField(widget= Dateinput)
    
    class Meta:
        model = Persona
        fields = ('__all__') # tambien con una tupla, ejemplo: ('nombre','apellido')
    def __init__(self, *args, **kwargs):
        super(Personaform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['required'] = 'required'  
            visible.field.widget.attrs['class'] = 'form-control is-invalid'