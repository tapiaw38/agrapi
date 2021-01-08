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
    orientation = models.CharField(max_length=20)
    building_material = models.CharField(max_length=50)
    roof_material = models.CharField(max_length=30)
    foor_material = models.CharField(max_length=30)
    surface = models.FloatField()
    num_animals = models.PositiveIntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
