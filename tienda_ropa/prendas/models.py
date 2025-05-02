from django.db import models

class Prenda(models.Model):
    TEMPORADAS = [
        ('primavera', 'Primavera'),
        ('verano', 'Verano'),
        ('otoño', 'Otoño'),
        ('invierno', 'Invierno'),
    ]

    nombre = models.CharField(max_length=100)
    temporada = models.CharField(max_length=10, choices=TEMPORADAS)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.temporada}"
