""" Model Producer Vehicle """

# Django
from django.db import models


class ProducerVehicle(models.Model):
    """Modelo de datos referidos a los vehiculos 
    vinculados con el productor"""

    producer = models.ForeignKey(
        "producer.Producer",
        related_name='producer_vehicle',
        on_delete=models.CASCADE
    )
    name_vehicle = models.CharField(max_length=50)
    domain = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    use_trailer = models.BooleanField(default=False)
    use_semitrailer = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.name_vehicle, self.producer)
