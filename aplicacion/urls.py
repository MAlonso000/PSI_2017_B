from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^medico/$', views.lista_alquileres, name='lista_alquileres'),
]
