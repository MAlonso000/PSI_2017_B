from django.contrib import admin
from aplicacion.models import Coche, Alquiler, Cliente

# Register your models here.
admin.site.register(Coche)
admin.site.register(Alquiler)
admin.site.register(Cliente)