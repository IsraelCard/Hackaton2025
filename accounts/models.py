from django.db import models
from django.contrib.auth.models import User

class Dispositivo(models.Model):
    TIPO_CHOICES = [
        ('sensor', 'Sensor'),
        ('electronico', 'Electrónico'),
        ('camara', 'Cámara'),
        ('foco','Foco/iluminacion'),
        ('electrodomestico','Electrodoméstio'),
        ('otros', 'Otros'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    estado = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    consumo = models.IntegerField(null=True,default=0)

    def __str__(self):
        return f"{self.nombre}"
    
class Registro(models.Model):
    idDispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    fechaRegistro = models.DateTimeField(auto_now=False)
    consumo = models.IntegerField(default=0,max_length=4)
    