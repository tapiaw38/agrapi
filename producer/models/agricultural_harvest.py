""" Production Agricultural Harvest """
# Django
from django.db import models


class AgriculturalHarvest(models.Model):
    """ Modelo de datos relacionado 
    con las cosecha de la producion """

    production_agricultural = models.OneToOneField(
        "producer.ProductionAgricultural",
        related_name="agricultural_harvest",
        on_delete=models.CASCADE
        )

    harvest_surface = models.FloatField()
    tons_production = models.FloatField()
    has_curtains_insulated = models.BooleanField()
    plant_length_curtains = models.FloatField(default=0)
    plant_species_curtains = models.CharField(max_length=100, blank=True, null=True)
    harvest_time = models.CharField(max_length=30)

    