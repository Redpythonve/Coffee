from django.db import models

class Products(models):
    name = models.TextField(max_length=250, verbose_name="nombre")
    description = models.TextField(max_length=350, verbose_name="descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2)
