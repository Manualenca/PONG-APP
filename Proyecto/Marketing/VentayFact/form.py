# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from VentayFact.models import Clientes
# from django.core.exceptions import ValidationError

# class FormClientes(forms.Form):
#     nombre = forms.CharField(
#         max_length= 20,
#         widget= forms.TextInput, 
#         requeried= True
#     )
#     apellido = forms.CharField(
#         max_length= 20,
#         widget= forms.TextInput,
#     )
#     email = forms.CharField(
#         widget= forms.EmailField, 
#     )
    
#     telefono = forms.NumberInput(
#         max_length = 15,
#         widget = forms.NumberInput
#     )
