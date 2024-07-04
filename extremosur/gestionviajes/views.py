# gestionviajes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm, RegistroClienteForm, PaqueteForm, ContactoForm
from .models import Carrito, PaqueteTuristico, FormularioContacto, Boleta
from django.contrib.auth import logout as auth_logout

def registro_cliente(request):
    if request.method == 'POST':
        usuario_form = RegistroUsuarioForm(request.POST)
        cliente_form = RegistroClienteForm(request.POST)
        if usuario_form.is_valid() and cliente_form.is_valid():
            user = usuario_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.usuario = user
            cliente.save()
            return redirect('index')
    else:
        usuario_form = RegistroUsuarioForm()
        cliente_form = RegistroClienteForm()
    return render(request, 'registro.html', {'usuario_form': usuario_form, 'cliente_form': cliente_form})

def agregar_paquete(request):
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            paquete = form.save()
            # Redirige al usuario a la página donde se listan los paquetes (ver_carrito)
            return redirect('ver_carrito')
    else:
        form = PaqueteForm()
    return render(request, 'agregar_paquete.html', {'form': form})


def agregar_al_carrito(request, paquete_id):
    cliente = request.user.cliente
    paquete = PaqueteTuristico.objects.get(id=paquete_id)
    carrito, created = Carrito.objects.get_or_create(cliente=cliente)
    carrito.paquetes.add(paquete)
    carrito.total += paquete.valor
    carrito.save()
    return redirect('ver_carrito')

def pago(request):
    cliente = request.user.cliente
    carrito = Carrito.objects.get(cliente=cliente)
    boleta = Boleta.objects.create(carrito=carrito)
    return render(request, 'boleta.html', {'boleta': boleta})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})


@login_required
def ver_carrito(request):
    try:
        cliente = request.user.cliente
        carrito, created = Carrito.objects.get_or_create(cliente=cliente)
    except Carrito.DoesNotExist:
        return redirect('index')  # Redirige al index si no existe carrito para este usuario

    return render(request, 'carrito.html', {'carrito': carrito})



@csrf_protect
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('ver_carrito')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def nuestros_servicios(request):
    return render(request, 'nuestros_servicios.html')