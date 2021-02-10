""" Production Agricultural Harvest """
# Django
from django.db import models
# utilities
from utils.models import ProduModel


class AgriculturalHarvest(ProduModel):
    """ Modelo de datos relacionado 
    con las cosecha de la producion """

    production_agricultural = models.ForeignKey(
        "producer.ProductionAgricultural",
        related_name="agricultural_harvest",
        on_delete=models.CASCADE
        )

    harvest_surface = models.FloatField(default=0)
    tons_production = models.FloatField(default=0)
    harvest_time = models.CharField(max_length=30, blank=True, null=True)

    