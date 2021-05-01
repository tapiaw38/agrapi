""" Model Production """

from django.db import models


class Production(models.Model):
    '''
    Type of Production that the producer develops,
    stores the producer's residence,
    road conditions and coordinates.
    '''

    producer = models.ForeignKey(
        "producer.Producer",
        related_name='production',
        on_delete=models.CASCADE
    )
    is_resident = models.BooleanField(default=False)
    district = models.CharField(max_length=50, blank=True, null=True)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    length_unit = models.IntegerField(default=0)
    surface = models.FloatField(default=0)
    road_state = models.CharField(max_length=200, blank=True, null=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    has_renspa = models.BooleanField(default=False)
    has_renaf = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.length_unit == 0:
            self.surface = (self.width * self.height) * 1
        elif self.length_unit == 1:
            self.surface = (self.width * self.height) * 10
        elif self.length_unit == 2:
            self.surface = (self.width * self.height) * 100
        elif self.length_unit == 3:
            self.surface = (self.width * self.height) * 1000
        else:
            return "A valid unit of measure was not selected."

        super(Production, self).save(*args, **kwargs)

    def __str__(self):
        return 'Producción {}'.format(self.producer)
