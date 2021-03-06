""" Production Livestock Beekeeping Cycle """

# Django
from django.db import models
# utilities
from utils.models import ProduModel

HIVES_CHOICES = (
    ('Propias','Propias'),
    ('Terceros','Terceros')
)
DROWER_CHOICES = (
    ('Fijos','Fijos'),
    ('Moviles','Moviles')
)

class LivestockBeekeepingCycle(ProduModel):
    """ Ciclo de apicultura de la 
    produccion ganadera """
    
    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_beekeeping_cycle",
        on_delete=models.CASCADE
        )
    renapa = models.BooleanField(default=False)
    kind_bee = models.CharField(max_length=100, blank=True, null=True)
    has_bee_hives = models.BooleanField(default=False)
    type_bee_hives = models.CharField(max_length=20, blank=True, null=True)
    number_drawers = models.PositiveIntegerField(default=0)
    alsas_drawer = models.PositiveIntegerField(default=0)
    pollination_period = models.CharField(max_length=50, blank=True, null=True)
    pollinated_flower = models.CharField(max_length=100, blank=True, null=True)