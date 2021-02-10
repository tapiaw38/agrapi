""" Production Livestock Woll Marketing """

# Django
from django.db import models
# utilities
from utils.models import ProduModel


class LivestockMarketing(ProduModel):
    """ Modelo de comercializacion 
    de lana y pelo de actividad ganadera """

    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_marketing",
        on_delete=models.CASCADE
        )
    number_slaughtered = models.PositiveIntegerField(default=0)
    slaughter_destination = models.CharField(max_length=100, blank=True, null=True)
    amount_leather = models.FloatField(default=0)
    leather_destination = models.CharField(max_length=100, blank=True, null=True)
    number_shorn = models.PositiveIntegerField(default=0)
    amount_wool = models.FloatField(default=0)
    wool_destination = models.CharField(max_length=100, blank=True, null=True)
    liters_milk = models.FloatField(default=0)
    milk_destination = models.CharField(max_length=100, blank=True, null=True)
    number_eggs = models.PositiveIntegerField(default=0)
    eggs_destination = models.CharField(max_length=100, blank=True, null=True)
    honey_yield = models.FloatField(default=0)
    honey_destination = models.CharField(max_length=100, blank=True, null=True)
    amount_feces = models.FloatField(default=0)
    feces_destination = models.CharField(max_length=100)
   



