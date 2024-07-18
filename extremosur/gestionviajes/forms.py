# gestionviajes/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Cliente, PaqueteTuristico, FormularioContacto

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'ciudad']

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = PaqueteTuristico
        fields = ['nombre_destino', 'fecha_viaje', 'valor']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = FormularioContacto
        fields = ['nombre', 'rut', 'ciudad', 'correo_electronico', 'consulta']

class BuscarPaqueteForm(forms.Form):
    query = forms.CharField(label='Buscar paquete', max_length=100)