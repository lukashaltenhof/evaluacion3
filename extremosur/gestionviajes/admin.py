# gestionviajes/admin.py

from django.contrib import admin
from .models import Cliente, PaqueteTuristico, Carrito, Boleta, FormularioContacto

admin.site.register(Cliente)
admin.site.register(PaqueteTuristico)
admin.site.register(Carrito)
admin.site.register(Boleta)
admin.site.register(FormularioContacto)
