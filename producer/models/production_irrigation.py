""" Production Irrigation """

#Django
from django.db import models


IRRIGATION_CHOICES = (
    ('Presurizado','Presurizado'),
    ('Superficial','Superficial')
)
PRESSURIZED_CHOICES = (
    ('Goteo','Goteo'),
    ('Aspersíon','Aspersíon'),
    ('Micro aspersión','Micro aspersión'),
)
SURFACE_CHOICES = (
    ('Inundación','Inundación'),
    ('Melga','Melga'),
    ('Caracol','Caracol'),
    ('Surcos','Surcos'),
    ('Terrazas','Terrazas'),
)
RIGHT_CHOICES = (
    ('Agua','Agua'),
    ('Eventualmente','Eventualmente')
)
SHIFTS_CHOICES = (
    ('Cortos','Cortos'),
    ('Medios','Medios'),
    ('Largos','Largos')
)


class ProductionIrrigation(models.Model):
    """ Modelo de riego de la produccion """

    production = models.OneToOneField(
        "producer.Production",
        related_name="production_irrigation",
        on_delete=models.CASCADE
        )
    type_irrigation = models.CharField(max_length=20, blank=True, null=True)
    pressurized_irrigation = models.CharField(max_length=20, blank=True, null=True)
    surface_irrigation = models.CharField(max_length=20, blank=True, null=True)
    take_section = models.CharField(max_length=20,blank=True, null=True)
    watering_hours = models.FloatField(default=0)
    channel_conditions = models.CharField(max_length=50, blank=True, null=True)
    right = models.CharField(max_length=20, blank=True, null=True)
    shifts = models.CharField(max_length=50, blank=True, null=True)