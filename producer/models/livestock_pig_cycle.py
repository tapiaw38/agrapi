""" Production Livestock Pig Cycle """

# Django
from django.db import models
# utilities
from utils.models import ProduModel

class LivestockPigCycle(ProduModel):
    """ Ciclo de cerdos relacionado 
    con la actividad productiva """
    
    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_pig_cycle",
        on_delete=models.CASCADE
        )
    up_three_months = models.PositiveIntegerField(default=0)
    three_eight_months = models.PositiveIntegerField(default=0)
    males_older_eight_months = models.PositiveIntegerField(default=0)
    females_older_eight_months = models.PositiveIntegerField(default=0)
    number_pigs = models.PositiveIntegerField(default=0)
    number_stallions = models.PositiveIntegerField(default=0)