""" Production Agroindustrial Tools """

# Django
from django.db import models


class AgroindustrialTools(models.Model):
    """ Modelo Herramientas del la 
    produccion Agroindustrial """

    production_agroindustrial = models.ForeignKey(
        "producer.ProductionAgroindustrial",
        related_name="agroindustrial_tools",
        on_delete=models.CASCADE
        )
    name_tool = models.CharField(max_length=50)
    type_tool = models.CharField(max_length=30)
    number_tools = models.PositiveIntegerField()
