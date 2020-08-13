from django import forms
from .models import Persona,Ciudad,TipoDocumento
from django.forms import ModelChoiceField

class MenuModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.nombre)

class Personaform(forms.ModelForm):
    lugarResidencia = MenuModelChoiceField(queryset=Ciudad.objects.all())
    idTipoDocumento = MenuModelChoiceField(queryset=TipoDocumento.objects.all())
    class Meta:
        model = Persona
        fields = ('__all__') # tambien con una tupla, ejemplo: ('nombre','apellido')