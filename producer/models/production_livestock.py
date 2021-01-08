""" Production Livestock """

# Django
from django.db import models


DESTINATIONS_CHOICES = (
    ("Venta","Venta"),
    ("Consumo","Consumo"),
    ("Ambos","Ambos"),
    ("Trueque","Trueque"),
    ("Otros","Otros")
)

class ProductionLivestock(models.Model):
    """ Modelos de producción ganadera"""

    production = models.ForeignKey(
        "producer.Production",
        related_name="production_livestock",
        on_delete=models.CASCADE)
    type_activity = models.CharField(max_length=30)
    surface = models.FloatField(default=0)
    destination = models.CharField(max_length=30)
    make_technical_assistance = models.BooleanField()
    problems = models.CharField(max_length=200, blank=True, null=True)
    suggestion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Producción Ganadera: {}'.format(self.production.producer)
