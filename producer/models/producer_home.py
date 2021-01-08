""" Producer Home Model """

# Django
from django.db import models


class ProducerHome(models.Model):
    """ Infrme social y condiciones de la vivienda del productor."""

    producer = models.OneToOneField(
        "producer.Producer",
        related_name='producer_home',
        on_delete=models.CASCADE
        )
    district = models.CharField(max_length=50) 
    address = models.CharField(max_length=50, help_text="Dirección particular")
    type_recidence = models.CharField(max_length=50, help_text="Tipo de recidencia")
    state_recidence = models.CharField(max_length=30)

    def __str__(self):
        return "Vivienda de {}".format(self.producer)