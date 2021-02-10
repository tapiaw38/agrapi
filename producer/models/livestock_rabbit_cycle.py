""" Production Livestock Rabbit Cycle """

# Django
from django.db import models
# utilities
from utils.models import ProduModel


class LivestockRabbitCycle(ProduModel):
    """ Ciclo de conejos de la produccion ganadera """

    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_rabbit_cycle",
        on_delete=models.CASCADE
        )
    orientation = models.CharField(max_length=20, blank=True, null=True)
    number_breeding_males = models.PositiveIntegerField(default=0)
    number_breeding_females = models.PositiveIntegerField(default=0)
    number_rabbit = models.PositiveIntegerField(default=0)