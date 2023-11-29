

from itertools import product
from django.shortcuts import render, redirect

from VentayFact.models import Productos
from .form import FormClientes

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login

# #nose
from django.contrib.auth.models import Group
from imaplib import _Authenticator
from django.contrib import messages # Para mensajes de sesión

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
    # datos = {'form': FormClientes(request.POST)}
    # return render (request, 'registrarse.html', datos)
    

#     def get (self, request):
#         form = UserCreationForm()
#         return render (request, 'registrarse.html', {"form" : form })
#         # datos = {'form': FormClientes(request.POST)}
#         # return render (request, 'registrarse.html', datos)
# #     def post(self, request): 
# #         form = UserCreationForm(request.post)

# #         if form.is_valid():

# #             usuario= form.save()

# #             login(request, usuario)

# #             return redirect('inicio')
        
# #         else: 
# #             pass

    if request.method == 'GET':
        return render(request, 'registrarse.html', {'form': FormClientes})

    if request.method == 'POST':
        form = FormClientes(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            group = Group.objects.get(name='Clientes')
            user.groups.add(group)

            # Autenticación manual del usuario creado
            user = _Authenticator(
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password1']       
            )
            login(request, user)

            # Redireccion a la pagina principal
            return redirect('inicio.html')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages)

                return render(request, "inicio.html", { "form", {form}})





# def carrito(request):
#     datos = {}
#     carrito = carro(request)
#     # carro = carrito.get_carrito()
#     print('carro', carrito.get_carrito())
#     return render (request, 'carrito.html', datos)

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

