

from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_cliente, name='registro_cliente'),
    path('agregar_paquete/', views.agregar_paquete, name='agregar_paquete'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:paquete_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('pago/', views.pago, name='pago'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('nuestros_servicios/', views.nuestros_servicios, name='nuestros_servicios'),
]
