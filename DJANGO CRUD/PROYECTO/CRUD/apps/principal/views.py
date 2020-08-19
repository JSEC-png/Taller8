from django.shortcuts import render, redirect
from .models import Persona
from .forms import Personaform

# Create your views here.
def index(request):
   
    personas = Persona.objects.all()
    return render(request,'index.html',{'personas':personas})


def crearPersona(request):
    if request.method == 'GET':
        form = Personaform()
        print(form.errors.as_data())
    else:
        form = Personaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors.as_data())
            return redirect('index')
    return render(request,'crear_persona.html',{'form':form})

def editarPersona(request,id):
    persona = Persona.objects.get(idPersona = id)
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
    return render(request,'crear_persona.html',contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(idPersona = id)
    persona.delete()
    return redirect('index')