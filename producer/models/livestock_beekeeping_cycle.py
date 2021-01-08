""" Production Livestock Beekeeping Cycle """

# Django
from django.db import models


HIVES_CHOICES = (
    ('Propias','Propias'),
    ('Terceros','Terceros')
)
DROWER_CHOICES = (
    ('Fijos','Fijos'),
    ('Moviles','Moviles')
)

class LivestockBeekeepingCycle(models.Model):
    """ Ciclo de apicultura de la 
    produccion ganadera """
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_beekeeping_cycle",
        on_delete=models.CASCADE
        )
    kind_bee = models.CharField(max_length=20, blank=True, null=True)
    has_bee_hives = models.BooleanField()
    type_bee_hives = models.CharField(max_length=20, blank=True, null=True)
    number_drawers = models.PositiveIntegerField(default=0)
    alsas_drawer = models.PositiveIntegerField(default=0)
    type_drawer = models.CharField(max_length=20, blank=True, null=True)
    honey_stones = models.PositiveIntegerField(default=0)
    pollination_period = models.CharField(max_length=50, blank=True, null=True)
    pollinated_flower = models.CharField(max_length=50, blank=True, null=True)
    has_renapa = models.BooleanField()