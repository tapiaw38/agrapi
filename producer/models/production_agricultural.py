""" Model Production Agricultural """

from django.db import models


class ProductionAgricultural(models.Model):
    """Modelo de produccion agricola, nombre, problemas, sugerecias"""
    production = models.ForeignKey(
        "producer.Production",
        related_name="production_agricultural",
        on_delete=models.CASCADE)
    name = models.CharField(max_length=15, default="Agricola")
    activity_name = models.CharField(max_length=50, blank=True, null=True) 
    surface = models.FloatField(default=0)
    destination = models.CharField(max_length=20, blank=True, null=True)
    sowing = models.CharField(max_length=20, blank=True, null=True)
    type_sowing = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveIntegerField(default=0)
    problems = models.CharField(max_length=100, blank=True, null=True)
    suggestion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Producción Agricola: {}'.format(self.production.producer)