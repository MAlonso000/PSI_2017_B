from django.shortcuts import render
from django.views import generic
from .models import Coche, Alquiler, Cliente

# Create your views here.

def lista_alquileres(request):

    context_dict = {}

    try:
        context_dict['coche'] = Coche.objects.get(id=1001)
        context_dict['alquileres'] = Alquiler.objects.filter(coche__id=1001)
        context_dict['error'] = None

    except BaseException:

        context_dict['error'] = "Coche no encontrado."
        context_dict['alquileres'] = None
        context_dict['coche'] = None

    return render(request, 'aplicacion/coche.html', context_dict)
