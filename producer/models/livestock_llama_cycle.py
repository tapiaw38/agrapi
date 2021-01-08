""" Production Livestock Llama Cycle """

# Django
from django.db import models


class LivestockLlamaCycle(models.Model):
    """ Ciclo de llamas 
    de la produccion Ganadera """
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_llama_cycle",
        on_delete=models.CASCADE
        )
    number_chitas_teques = models.PositiveIntegerField(default=0)
    number_maltones = models.PositiveIntegerField(default=0)
    number_janachos = models.PositiveIntegerField(default=0)
    number_llamas_mothers = models.PositiveIntegerField(default=0)
    number_capons = models.PositiveIntegerField(default=0)