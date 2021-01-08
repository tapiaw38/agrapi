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
    use_trailer = models.BooleanField()
    type_trailer = models.CharField(max_length=50, blank=True, null=True)
    use_semitrailer = models.BooleanField()

    def __str__(self):
        return '{} {}'.format(self.name_vehicle, self.producer)