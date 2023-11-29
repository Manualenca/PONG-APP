from django.urls import path, include
from VentayFact import views
# from .views import login_view
from django.contrib import admin

urlpatterns = [
    
    path('contacto/', views.contacto, name='contacto'),
    path('campanas/', views.campanas, name='campanas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('proyectos/', views.proyectos, name='proyectos'),

    path('tipocamp/', views.tipocamp, name='tipocamp'),
    # path('login/', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrarse', views.registrarse, name='registrarse'),
    path('carrito/', views.carro, name= 'carrito'),
    
    path('admin/', admin.site.urls),
    path('', views.inicio, name = 'inicio'),
]
