""" Model Production """

from django.db import models


class Production(models.Model):
    '''Tipo de Produccion que desarrolla el productor, 
    almacena la recidencia del productor, 
    condiciones de los caminos y coordendas.'''

    producer = models.ForeignKey(
        "producer.Producer",
        related_name='production',
        on_delete=models.CASCADE
        )
    is_resident = models.BooleanField()
    district = models.CharField(max_length=50)
    surface = models.FloatField()
    road_state = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()
    has_renspa = models.BooleanField()

    def __str__(self):
        return 'Producción {}'.format(self.producer)

