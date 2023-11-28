from django.shortcuts import render
from .form import FormClientes


def inicio(request):
    datos = {}
    return render (request, 'index.html', datos)

def contacto(request):
    datos = {}
    return render (request, 'contacto.html', datos)


def campanas(request):
    datos = {}
    return render (request, 'campanas.html', datos)

def nosotros(request):
    datos = {}
    return render (request, 'nosotros.html', datos)

def proyectos(request):
    datos = {}
    return render (request,'proyectos.html', datos)

def tipocamp(request):
    datos = {}
    return render (request,'tipocamp.html', datos)

def login(request):
    datos = {}
    return render (request,'login.html', datos)

def registrarse(request):
    datos = {'form': FormClientes(request.POST)}
    return render (request, 'registrarse.html', datos)

def carrito(request):
    datos = {}
    return render (request, 'carrito.html', datos)