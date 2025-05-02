from django.core.management.base import BaseCommand
from prendas.models import Prenda

class Command(BaseCommand):
    help = 'Llena la base de datos con prendas de prueba'

    def handle(self, *args, **kwargs):
        datos_prendas = [
            {"nombre": "Camisa de lino", "temporada": "verano", "precio": 45.00},
            {"nombre": "Bermuda de algodón", "temporada": "verano", "precio": 35.00},
            {"nombre": "Suéter ligero", "temporada": "otoño", "precio": 50.00},
            {"nombre": "Chaqueta gruesa", "temporada": "invierno", "precio": 120.00},
            {"nombre": "Vestido floral", "temporada": "primavera", "precio": 70.00},
        ]

        for datos in datos_prendas:
            Prenda.objects.create(**datos)

        self.stdout.write(self.style.SUCCESS("¡Base de datos poblada con prendas de prueba!"))
