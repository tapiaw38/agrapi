""" Production Livestock Health """

from django.db import models


TECHNICAL_CHOICES = (
    ('Privada','Privada'),
    ('Publica','Publica')
)
DISEASE_CHOICES = (
    ('Propias','Propias'),
    ('Zoonoticas','Zoonoticas')
)

class LivestockHealth(models.Model):
    """ Modelo Sanidad, vacunas y enfermedades del tipo de ganado"""

    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_health",
        on_delete=models.CASCADE
        )
    type_technical_assistance = models.CharField(max_length=20)
    vitamin_complex = models.CharField(max_length=30, blank=True, null=True)
    make_internal_deworming = models.BooleanField()
    make_external_deworming = models.BooleanField()
    type_antiparasitic = models.CharField(max_length=30, blank=True, null=True)
    make_vaccination = models.BooleanField()
    type_vaccination = models.CharField(max_length=30, blank=True, null=True)
    type_disease = models.CharField(max_length=20, blank=True, null=True)
    other_practices = models.CharField(max_length=100, blank=True, null=True)