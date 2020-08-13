from django.shortcuts import render, redirect
from .models import Persona
from .forms import Personaform

# Create your views here.
def index(request):
    if request.method == 'GET':
        form = Personaform()
    else:
        form = Personaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'index.html',{'form':form})


def crearPersona(request):
    if request.method == 'GET':
        form = Personaform()
    else:
        form = Personaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('NO PUEDE SER')
            return redirect('index')
    return render(request,'index.html',{'form':form})

def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = Personaform(instance= persona)
        contexto = {
            'form':form
        }
    else:
        form = Personaform(request.POST, instance= persona)
        if form.is_valid():
            form.save()
            contexto = {
                'form':form
            }
            return redirect('index')
    return render(request,'crearPersona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')