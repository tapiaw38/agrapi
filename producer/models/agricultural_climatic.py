""" Production Agricultural Climatic Factore """

from django.db import models


DAMANGE_CHOICES = (
    ("Alto","Alto"),
    ("Medio","Medio"),
    ("Bajo","Bajo"),
    ("Nulo","Nulo")
)

class AgriculturalClimatic(models.Model):
    """ Modelo de factores climicticos y daños 
     que afectan a la produccion """
     
    production_agricultural = models.ForeignKey(
        "producer.ProductionAgricultural",
        related_name="agricultural_climatic",
        on_delete=models.CASCADE
        )
    factor = models.CharField(max_length=100)
    risk = models.CharField(max_length=50)
    damange_level = models.CharField(max_length=50)
