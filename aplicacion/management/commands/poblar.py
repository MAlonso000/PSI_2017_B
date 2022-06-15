# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data
# (https://zetcode.com/python/faker/)
import os

from django.core.management.base import BaseCommand
from aplicacion.models import (Coche, Alquiler, Cliente)
# from django.contrib.auth.models import User
from faker import Faker
# define STATIC_PATH in settings.py
# from proyecto.settings import STATIC_PATH
# from PIL import Image, ImageDraw, ImageFont
# from django.contrib.auth.hashers import make_password
from django.utils.dateparse import parse_date


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.cleanDataBase()   # clean database
        self.coche()
        self.cliente()
        self.alquiler()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        Coche.objects.all().delete()
        Alquiler.objects.all().delete()
        Cliente.objects.all().delete()

    def coche(self):

        coche = {}

        coche[1] = {'id': 1001,
                    'modeloC': 'coche1',}
        coche[2] = {'id': 1002,
                    'modeloC': 'coche2',}
        coche[3] = {'id': 1003,
                    'modeloC': 'coche3',}

        for index, a in enumerate(coche.values()):
            x = Coche.objects.get_or_create(
                id=a['id'],
                modeloC=a['modeloC']
            )[0]
            x.save()

    def cliente(self):

        cliente = {}

        cliente[1] = {'id': 1001,
                      'nombreC': 'cliente1',}
        cliente[2] = {'id': 1002,
                      'nombreC': 'cliente2',}
        cliente[3] = {'id': 1003,
                      'nombreC': 'cliente3',}
        cliente[4] = {'id': 1004,
                      'nombreC': 'cliente4',}

        for index, a in enumerate(cliente.values()):
            x = Cliente.objects.get_or_create(
                id=a['id'],
                nombreC=a['nombreC'],
            )[0]
            x.save()

    def alquiler(self):

        alquiler = {}

        alquiler[1] = {'id': 1001,
                      'coche': 1001,
                      'cliente': 1001,
                      'duracion': 1, }
        alquiler[2] = {'id': 1002,
                      'coche': 1002,
                      'cliente': 1002,
                      'duracion': 2, }
        alquiler[3] = {'id': 1003,
                      'coche': 1002,
                      'cliente': 1003,
                      'duracion': 3, }
        alquiler[4] = {'id': 1004,
                      'coche': 1001,
                      'cliente': 1003,
                      'duracion': 4, }

        for index, a in enumerate(alquiler.values()):
            x = Alquiler.objects.get_or_create(
                id=a['id'],
                coche=Coche.objects.get(id=int(a['coche'])),
                cliente=Cliente.objects.get(id=int(a['cliente'])),
                duracion=a['duracion']
            )[0]
            x.save()