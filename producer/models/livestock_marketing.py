""" Production Livestock Woll Marketing """

# Django
from django.db import models


class LivestockMarketing(models.Model):
    """ Modelo de comercializacion 
    de lana y pelo de actividad ganadera """

    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_marketing",
        on_delete=models.CASCADE
        )
    number_slaughtered = models.PositiveIntegerField(default=0)
    number_shorn = models.PositiveIntegerField(default=0)
    amount_wool_hair = models.PositiveIntegerField(default=0)
    amount_leather = models.PositiveIntegerField(default=0)
    liters_milk = models.PositiveIntegerField(default=0)
    milk_destination = models.CharField(max_length=100, blank=True, null=True)
    wool_hair_destination = models.CharField(max_length=100, blank=True, null=True)
    leather_destination = models.CharField(max_length=100, blank=True, null=True)
    slaughter_destination = models.CharField(max_length=100, blank=True, null=True)



