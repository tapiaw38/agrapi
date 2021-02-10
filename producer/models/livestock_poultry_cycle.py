""" Produccion Livestock Poultry Cycle """

# Django
from django.db import models
# utilities
from utils.models import ProduModel


class LivestockPoultryCycle(ProduModel):
    """ Ciclo Avicola 
    de la produccion ganadera """
    
    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_poultry_cycle",
        on_delete=models.CASCADE
        )
    is_intensive_poultry = models.BooleanField(default=False)
    has_hatchery = models.BooleanField(default=False)
    number_incubators = models.PositiveIntegerField(default=0)
    number_hatching_eggs = models.PositiveIntegerField(default=0)
    chicks_one_two_months = models.PositiveIntegerField(default=0)
    chicks_three_five_months = models.PositiveIntegerField(default=0)
    females_older_six_months = models.PositiveIntegerField(default=0)
    number_broiler_chickens = models.PositiveIntegerField(default=0)
    number_breeder_layers = models.PositiveIntegerField(default=0)
    number_breeding_males = models.PositiveIntegerField(default=0)
    
