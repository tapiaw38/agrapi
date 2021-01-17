""" Livestock Animal Pens """

#Django
from django.db import models


ORIENTATION_CHOICES = (
    ('Norte','Norte'),
    ('Sur','Sur'),
    ('Este','Este'),
    ('Oeste','Oeste')
)

class LivestockAnimalPens(models.Model):
    """ Modelo de Corrales de animales
    de la produccion ganadera """
    
    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_animal_pens",
        on_delete=models.CASCADE
        )
    orientation = models.CharField(max_length=20, blank=True, null=True)
    building_material = models.CharField(max_length=50, blank=True, null=True)
    roof_material = models.CharField(max_length=30, blank=True, null=True)
    foor_material = models.CharField(max_length=30, blank=True, null=True)
    surface = models.FloatField(default=0)
    num_animals = models.PositiveIntegerField(default=0)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
