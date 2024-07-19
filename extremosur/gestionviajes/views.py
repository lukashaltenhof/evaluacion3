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
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json


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


@login_required
def agregar_al_carrito(request, paquete_id):
    print("Before adding, cart:", request.session.get('carrito', 'Cart is empty'))

    if not str(paquete_id).isdigit():
        return HttpResponseBadRequest("Invalid item ID")

    paquete_id = int(paquete_id)
    carrito = request.session.get('carrito', {})

    if paquete_id in carrito:
        carrito[paquete_id] += 1
    else:
        carrito[paquete_id] = 1

    request.session['carrito'] = carrito
    request.session.modified = True

    print("After adding, cart:", request.session['carrito'])

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
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})


@login_required
def ver_carrito(request):
    carrito_session = request.session.get('carrito', {})
    carrito_items = []
    total = 0

    for item_id, cantidad in carrito_session.items():
        if not str(item_id).isdigit():
            # Handle invalid item_id (e.g., log, skip, etc.)
            continue  # Skip this iteration if item_id is not a valid digit

        item_id = int(item_id)  # Convert item_id to integer
        item = get_object_or_404(PaqueteTuristico, id=item_id)
        total_item = item.valor * cantidad
        total += total_item
        carrito_items.append((item, cantidad))

    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total': total})


@csrf_protect
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
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


def paquete_list(request):
    paquetes = PaqueteTuristico.objects.all()
    paginator = Paginator(paquetes, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'paquete_list.html', {'page_obj': page_obj})

# Detalle de paquete turístico
@staff_member_required
def paquete_detail(request, id):
    paquete = get_object_or_404(PaqueteTuristico, id=id)
    return render(request, 'paquete_detail.html', {'paquete': paquete})

# Crear paquete turístico
@staff_member_required
def paquete_create(request):
    if request.method == 'POST':
        form = PaqueteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paquete_list')
    else:
        form = PaqueteForm()
    return render(request, 'paquete_form.html', {'form': form})

# Actualizar paquete turístico
@staff_member_required
def paquete_update(request, id):
    paquete = get_object_or_404(PaqueteTuristico, id=id)
    if request.method == 'POST':
        form = PaqueteForm(request.POST, instance=paquete)
        if form.is_valid():
            form.save()
            return redirect('paquete_list')
    else:
        form = PaqueteForm(instance=paquete)
    return render(request, 'paquete_form.html', {'form': form})

# Eliminar paquete turístico
@staff_member_required
def paquete_delete(request, id):
    paquete = get_object_or_404(PaqueteTuristico, id=id)
    if request.method == 'POST':
        paquete.delete()
        return redirect('paquete_list')
    return render(request, 'paquete_confirm_delete.html', {'paquete': paquete})

@staff_member_required
def contacto_list(request):
    contactos = FormularioContacto.objects.all()
    return render(request, 'contacto_list.html', {'contactos': contactos})

@staff_member_required
def contacto_detail(request, id):
    contacto = get_object_or_404(FormularioContacto, id=id)
    return render(request, 'contacto_detail.html', {'contacto': contacto})

@staff_member_required
def contacto_create(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_list')
    else:
        form = ContactoForm()
    return render(request, 'contacto_form.html', {'form': form})

@staff_member_required
def contacto_update(request, id):
    contacto = get_object_or_404(FormularioContacto, id=id)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('contacto_list')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contacto_form.html', {'form': form})

@staff_member_required
def contacto_delete(request, id):
    contacto = get_object_or_404(FormularioContacto, id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('contacto_list')
    return render(request, 'contacto_confirm_delete.html', {'contacto': contacto})


def vista_paquetes_cliente(request):
    query = request.GET.get('query')
    paquetes = PaqueteTuristico.objects.all()

    if query:
        paquetes = paquetes.filter(
            Q(nombre_destino__icontains=query)
        )

    paginator = Paginator(paquetes, 6)  # Mostrar 6 paquetes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Si es una solicitud AJAX, devolvemos solo el contenido de los paquetes
        context = {
            'page_obj': page_obj,
            'query': query,
        }
        html_response = render(request, 'paquetes_partial.html', context).content.decode('utf-8')
        return JsonResponse(html_response, safe=False)

    # Si no es AJAX, renderizamos la página completa
    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'vista_paquetes_cliente.html', context)

@login_required
def add_to_cart_view(request, item_id):
    paquete = get_object_or_404(Paquete, id=item_id)
    # Assuming you have a Cart model or a session-based cart
    # This is a placeholder for the logic to add the item to the cart
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_view_url_name')


@require_POST
def modify_quantity(request):
    # Assuming the cart is stored in the session
    data = json.loads(request.body)
    action = data['action']
    item_id = data['itemId']
    
    # Modify the quantity in the session
    carrito = request.session.get('carrito', {})
    if item_id in carrito:
        if action == 'increase':
            carrito[item_id]['cantidad'] += 1
        elif action == 'decrease' and carrito[item_id]['cantidad'] > 1:
            carrito[item_id]['cantidad'] -= 1
    
    request.session['carrito'] = carrito
    
    # Return a response
    return JsonResponse({'success': True, 'newQuantity': carrito[item_id]['cantidad']})

@require_POST
def clear_cart(request):
    if 'carrito' in request.session:
        del request.session['carrito']
    return JsonResponse({'success': True})