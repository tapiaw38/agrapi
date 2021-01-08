""" Livestok Animal Feeding """

#Django
from django.db import models


FEEDING_CHOICES=(
    ("Compra","Compra"),
    ("Trueque","Trueque"),
    ("Donaciones","Donaciones"),
    ("Naturales","Naturales"),
)

class LivestockAnimalFeeding(models.Model):
    """ Modelo de Alimentcion animal 
    de la produccion Ganadera """

    production_livestock = models.ForeignKey(
        "producer.ProductionLivestock",
        related_name="livestock_animal_feeding",
        on_delete=models.CASCADE
        )
    feeding = models.CharField(max_length=30)
    type_feeding = models.CharField(max_length=30)
    daily_rations = models.FloatField()