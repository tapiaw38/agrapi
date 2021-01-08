""" Production Agricultural Machine """

from django.db import models


MAQUINARY_CHOICES = (
    ("Propia","Propia"),
    ("Alquilada","Alquilada"),
    ("Prestada","Prestada"),
)
DESTINATINON_CHOICES = (
    ("Producción Aricola","Producción Aricola"),
    ("Producción Ganadera","Producción Ganadera"),
    ("Producción Agro-Industrial","Produccón Agro-Industrial")
)

class ProductionMachine(models.Model):
    """Tipo de maquinaria 
    segun el tipo de actividad agricola"""

    production = models.ForeignKey(
        "producer.Production",
        related_name="production_machine",
        on_delete=models.CASCADE
        )
    destination = models.CharField(max_length=30)
    name_machine = models.CharField(max_length=100)
    type_maquinary = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    state_machine = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    observation = models.CharField(max_length=100,blank=True, null=True)