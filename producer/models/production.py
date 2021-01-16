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
    is_resident = models.BooleanField(default=False)
    district = models.CharField(max_length=50)
    surface = models.FloatField(default=0)
    road_state = models.CharField(max_length=200,blank=True, null=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    has_renspa = models.BooleanField(default=False)

    def __str__(self):
        return 'Producción {}'.format(self.producer)

