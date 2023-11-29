from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
# from VentayFact.models import Clientes

class FormClientes(UserCreationForm):
    nombre = forms.CharField(required=True)
    apellido = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefono = forms.CharField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    