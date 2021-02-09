""" Production Livestock Llama Cycle """

# Django
from django.db import models


class LivestockLlamaCycle(models.Model):
    """ Ciclo de llamas 
    de la produccion Ganadera """
    
    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_llama_cycle",
        on_delete=models.CASCADE
        )
    number_tekes = models.PositiveIntegerField(default=0)
    number_tekes_weaned = models.PositiveIntegerField(default=0)
    number_maltones = models.PositiveIntegerField(default=0)
    number_young_females = models.PositiveIntegerField(default=0)
    number_young_males = models.PositiveIntegerField(default=0)
    number_llamas_mothers = models.PositiveIntegerField(default=0)
    number_capons = models.PositiveIntegerField(default=0)