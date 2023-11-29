from django.urls import path
from VentayFact import views

urlpatterns = [
    path('', views.inicio, name = 'inicio'),

    path('contacto/', views.contacto, name='contacto'),
    path('campanas/', views.campanas, name='campanas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('proyectos/', views.proyectos, name='proyectos'),

    path('tipocamp/', views.tipocamp, name='tipocamp'),
    path('proyecto/login', views.login, name='login'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('carrito/', views.carrito, name= 'carrito'),
]
