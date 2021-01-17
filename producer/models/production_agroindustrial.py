""" Agrindustrial Production """

# Django
from django.db import models

class ProductionAgroindustrial(models.Model):
    """ Produccion agroindustrial """

    production = models.ForeignKey(
        "producer.Production",
        related_name="production_agroindustrial",
        on_delete=models.CASCADE
        )
    description = models.CharField(max_length=50, blank=True, null=True)
    raw_material = models.CharField(max_length=20, blank=True, null=True)
    is_mechanized = models.BooleanField(default=False)
    knowledge = models.CharField(max_length=30, blank=True, null=True)