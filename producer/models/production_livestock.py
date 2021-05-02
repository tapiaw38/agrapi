""" Production Livestock """

# Django
from django.db import models


class ProductionLivestock(models.Model):
    """ 
    Models production livestock.
    """

    production = models.ForeignKey(
        "producer.Production",
        related_name="production_livestock",
        on_delete=models.CASCADE)
    type_activity = models.CharField(max_length=30, blank=True, null=True)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    length_unit = models.IntegerField(default=0)
    surface = models.FloatField(default=0)
    destination = models.CharField(max_length=30, blank=True, null=True)
    make_technical_assistance = models.BooleanField(default=False)
    problems = models.CharField(max_length=200, blank=True, null=True)
    suggestion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Producción Ganadera: {}'.format(self.production)

    def save(self, *args, **kwargs):
        """
        calculate length measurement before saving.
        3 -> kilometer (km) = 1000 m
        2 -> hectometer (hm) 100 m
        1 -> decameter (dam) 10 m
        0 -> meter (m) = 1 m
        """
        if self.length_unit == 0:
            self.surface = (self.width * self.height) * 1
        elif self.length_unit == 1:
            self.surface = (self.width * self.height) * 10
        elif self.length_unit == 2:
            self.surface = (self.width * self.height) * 100
        elif self.length_unit == 3:
            self.surface = (self.width * self.height) * 1000
        else:
            return "Length unit no valid"

        # Call the real save() method
        super(ProductionLivestock, self).save(*args, **kwargs)
