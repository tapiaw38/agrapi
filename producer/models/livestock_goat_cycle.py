""" Production Livestock Goat Cycle """

# Django
from django.db import models


class LivestockGoatCycle(models.Model):
    """ Modelo del ciclo parino 
    de la produccion ganadera"""
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_goat_cycle",
        on_delete=models.CASCADE
        )
    goats_under_six_months = models.PositiveIntegerField(default=0)
    goats_six_months_to_first_calving = models.PositiveIntegerField(default=0)
    number_goats = models.PositiveIntegerField(default=0)
    number_capons = models.PositiveIntegerField(default=0)
    number_stallions = models.PositiveIntegerField(default=0)