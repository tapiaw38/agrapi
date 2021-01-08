""" Produccion Livestock Poultry Cycle """

# Django
from django.db import models


class LivestockPoultryCycle(models.Model):
    """ Ciclo Avicola 
    de la produccion ganadera """
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_poultry_cycle",
        on_delete=models.CASCADE
        )
    is_intensive_poultry = models.BooleanField()
    number_broilers_incubated = models.PositiveIntegerField(default=0)
    breeding_males = models.PositiveIntegerField(default=0)
    number_eggs_chickens_babies = models.PositiveIntegerField(default=0)
    number_incubators = models.PositiveIntegerField(default=0)
    number_broilers_fattening = models.PositiveIntegerField(default=0)
    number_breeding_layers = models.PositiveIntegerField(default=0)
    existence = models.CharField(max_length=50, blank=True, null=True)
    
