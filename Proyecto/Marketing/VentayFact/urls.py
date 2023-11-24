from django.urls import path
from VentayFact import views

urlpatterns = [
    path('', views.Funcion, name = 'inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('campanas/', views.campanas, name='campanas'),
    path('nosotros/', views.nosotros, name='nosotros'),
]
