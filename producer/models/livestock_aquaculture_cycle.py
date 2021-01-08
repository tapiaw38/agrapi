""" Production Livestock Acuaculture Cycle """

# Django
from django.db import models


class LivestockAquacultureCycle(models.Model):
    """ Ciclo de acuicultura de la produccion ganadera """

    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_aquaculture_cycle",
        on_delete=models.CASCADE
        )
    orientation = models.CharField(max_length=30, blank=True, null=True)
    existence = models.CharField(max_length=50, blank=True, null=True)