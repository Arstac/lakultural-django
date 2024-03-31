from django.db import models
from usuarios.models import Usuario

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='eventos/', null=True, blank=True)
    organizador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos_organizados')  # Relación con Usuario

    def __str__(self):
        return self.nombre