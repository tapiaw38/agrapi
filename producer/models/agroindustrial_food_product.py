""" Prouction Agroindustrial Food Product """

# Django 
from django.db import models


class AgroindustrialFoodProduct(models.Model):
    """ Modelo Productos Alimentarios 
    de la produccion agrondustrial """

    production_agroindustrial = models.ForeignKey(
        "producer.ProductionAgroindustrial",
        related_name="agroindustrial_food_product",
        on_delete=models.CASCADE
        )
    name_product = models.CharField(max_length=50)
    origin = models.CharField(max_length=30)
    validity = models.CharField(max_length=30)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)