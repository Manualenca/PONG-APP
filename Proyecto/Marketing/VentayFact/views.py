from itertools import product
from django.shortcuts import render

from VentayFact.models import Productos
from .form import FormClientes
#EXEQUIEL
from .carro import carro
from django.shortcuts import redirect



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
    carrito = carro(request)
    # carro = carrito.get_carrito()
    print('carro', carrito.get_carrito())
    return render (request, 'carrito.html', datos)

# EXEQUIEL

def agregar_producto(request, producto_id):

    carro=carro(request)

    producto=Productos.objects.get(id=producto_id)

    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):

    carro=carro(request)

    producto=producto.objects.get(id=producto_id)

    carro.eliminar(producto=Productos)
    return redirect("tienda")

def restar_producto(request, producto_id):

    carro=carro(request)

    producto=Productos.objects.get(id=producto_id)

    carro.restar(producto=Productos)
    return redirect("tienda")

# def carrito(request):
#     print(request)
    # carro = carro(request)
    # print(carro)
    # items = carro.get_items()
    # datos = {'items': items}
    # return render(request, 'carrito.html', datos)

