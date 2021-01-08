""" Production Livestock Pig Cycle """

# Django
from django.db import models

class LivestockPigCycle(models.Model):
    """ Ciclo de cerdos relacionado 
    con la actividad productiva """
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_pig_cycle",
        on_delete=models.CASCADE
        )
    up_two_months = models.PositiveIntegerField(default=0)
    older_two_months = models.PositiveIntegerField(default=0)
    less_four_months = models.PositiveIntegerField(default=0)
    older_four_months = models.PositiveIntegerField(default=0)
    number_pigs = models.PositiveIntegerField(default=0)
    number_stallions = models.PositiveIntegerField(default=0)