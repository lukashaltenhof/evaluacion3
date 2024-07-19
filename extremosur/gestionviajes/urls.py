from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path('agregar_paquete/', views.agregar_paquete, name='agregar_paquete'),
    path('ver-carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:paquete_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('pago/', views.pago, name='pago'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('nuestros_servicios/', views.nuestros_servicios, name='nuestros_servicios'),
    path('paquetes/', views.paquete_list, name='paquete_list'),
    path('paquetes/<int:id>/', views.paquete_detail, name='paquete_detail'),
    path('paquetes/create/', views.paquete_create, name='paquete_create'),
    path('paquetes/update/<int:id>/', views.paquete_update, name='paquete_update'),
    path('paquetes/delete/<int:id>/', views.paquete_delete, name='paquete_delete'),
    path('contactos/', views.contacto_list, name='contacto_list'),
    path('contactos/<int:id>/', views.contacto_detail, name='contacto_detail'),
    path('contactos/create/', views.contacto_create, name='contacto_create'),
    path('contactos/update/<int:id>/', views.contacto_update, name='contacto_update'),
    path('contactos/delete/<int:id>/', views.contacto_delete, name='contacto_delete'),
    path('vista_paquetes_cliente/', views.vista_paquetes_cliente, name='vista_paquetes_cliente'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:item_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('path/to/clear_cart/', views.clear_cart, name='clear_cart'),
]
