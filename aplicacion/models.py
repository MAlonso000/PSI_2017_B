
from django.db import models

# Create your models here.

class Coche(models.Model):

    modeloC = models.CharField(max_length=100)

    class Meta:
        ordering = ['modeloC']

    def __str__(self):
        return self.modeloC


class Cliente(models.Model):

    nombreC = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombreC']

    def __str__(self):
        return self.nombreC


class Alquiler(models.Model):

    coche = models.ForeignKey(Coche, on_delete=models.SET_NULL, null=True, related_name='alquileres')

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name='alquileres')

    duracion = models.IntegerField(
            default=0
        )

    class Meta:
        ordering = ['coche', 'cliente']

    def __str__(self):
        return 'Alquiler - %s, %s: %s' % (self.coche, self.cliente, self.duracion)