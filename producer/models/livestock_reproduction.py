""" Production Livestock Reproduction """

from django.db import models


class LivestockReproduction(models.Model):
    """ Modelo de reproduccion de de la actividad ganadera"""
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_reproduction",
        on_delete=models.CASCADE
        )
    make_reproductive_management = models.BooleanField(default=False)
    type_reproductive_management = models.CharField(max_length=50, blank=True, null=True)
    make_continuous_service = models.BooleanField(default=False)
    other_practices = models.CharField(max_length=100, blank=True, null=True)
