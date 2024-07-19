from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username

class PaqueteTuristico(models.Model):
    nombre_destino = models.CharField(max_length=100)
    fecha_viaje = models.DateField()
    valor = models.IntegerField()  # Cambiado a IntegerField para no tener decimales
    imagen = models.ImageField(upload_to='imagenes_paquetes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_destino} - ${self.valor}"

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    paquetes = models.ManyToManyField(PaqueteTuristico, through='CarritoPaquete')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def total_price(self):
        return sum(item.subtotal() for item in self.carritopaquete_set.all())

class CarritoPaquete(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    paquete = models.ForeignKey('PaqueteTuristico', on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def subtotal(self):
        return self.paquete.valor * self.cantidad

class Boleta(models.Model):
    carrito = models.OneToOneField(Carrito, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    ciudad = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    consulta = models.TextField()

    def __str__(self):
        return self.nombre