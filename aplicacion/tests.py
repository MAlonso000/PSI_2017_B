from django.test import TestCase, Client
from .models import Coche, Alquiler, Cliente
from decimal import Decimal
from django.urls import reverse


class AplicacionTest(TestCase):

    def setUp(self):
        self.coche = {
            "id": 1001,
            "modeloC": 'coche1'
        }
        self.cliente1 = {
            "id": 1001,
            "nombreC": "cliente1"
        }
        self.cliente2 = {
            "id": 1002,
            "nombreC": "cliente2"
        }

    @classmethod
    def decode(cls, txt):
        return txt.decode("utf-8")

    def create_check(self, dictionary, ObjectClass):
        """ create an object of the class 'ObjectClass'
        using the dictionary. Then,
        check that all key-values in the
        dictionary are attributes in the object.
        return created object of class Object
        """
        # check that str function exists
        self.assertTrue(ObjectClass.__str__ is not object.__str__)
        # create object
        item = ObjectClass.objects.create(**dictionary)
        for key, value in dictionary.items():
            self.assertEqual(getattr(item, key), value)
        # execute __str__() so all the code in models.py is checked
        item.__str__()
        return item

    def test01(self):

        coche = self.create_check(self.coche, Coche)
        cliente1 = self.create_check(self.cliente1, Cliente)
        cliente2 = self.create_check(self.cliente2, Cliente)

        self.alquiler = {
            "id": 1001,
            "coche": coche,
            "cliente": cliente2,
            "duracion": 3
        }

        alquiler = self.create_check(self.alquiler, Alquiler)

        response = self.client.get(
                reverse("lista_alquileres"),
                follow=True)
        response_txt = self.decode(response.content)
        self.assertFalse(response_txt.find("Clientes que han alquilado el coche modelo 1001 con identificador") == -1)