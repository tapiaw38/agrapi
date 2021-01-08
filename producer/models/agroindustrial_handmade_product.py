""" Prouction Agroindustrial Handmade Product """

# Django 
from django.db import models


class AgroindustrialHandmandeProduct(models.Model):
    """ Modelo Productos Alimentarios 
    de la produccion agrondustrial """

    production_agroindustrial = models.ForeignKey(
        "producer.ProductionAgroindustrial",
        related_name="agroindustrial_handmande_product",
        on_delete=models.CASCADE
        )
    name_product = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)