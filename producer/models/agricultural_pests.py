""" Production Agricultural Pests """

from django.db import models

PESTS_CHOICES = (
    ('Enfermedad','Enfermedad'),
    ('Plaga','Plaga'),
    ('Maleza','Maleza')
)


class AgriculturalPests(models.Model):
    """ Pestes, plagas y enfermedados 
    de la actividad agricultural """
    
    production_agricultural = models.ForeignKey(
        "producer.ProductionAgricultural",
        related_name="agricultural_pests",
        on_delete=models.CASCADE
        )
    type_pests = models.CharField(max_length=20,blank=True, null=True)
    pests_description = models.CharField(max_length=100, blank=True, null=True)
    make_pests_control = models.BooleanField(default=False)
    type_pests_control = models.CharField(max_length=30)
    make_pesticide = models.BooleanField(default=False)
    type_pesticide = models.CharField(max_length=40, blank=True, null=True)
    other_practices= models.CharField(max_length=120, blank=True, null=True)