from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Persona
from .forms import Personaform
from django.urls import reverse_lazy

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = Personaform
    template_name = 'crearPersona.html'
    success_url = reverse_lazy('index')