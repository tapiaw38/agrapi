""" Model Production Agricultural """

from django.db import models


class ProductionAgricultural(models.Model):
    """Modelo de produccion agricola, nombre, problemas, sugerecias"""
    production = models.ForeignKey(
        "producer.Production",
        related_name="production_agricultural",
        on_delete=models.CASCADE)
    name = models.CharField(max_length=15, default="Agricola")
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    variety = models.CharField(max_length=50, blank=True, null=True)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    length_unit = models.IntegerField(default=0)
    surface = models.FloatField(default=0)
    destination = models.CharField(max_length=20, blank=True, null=True)
    sowing = models.CharField(max_length=20, blank=True, null=True)
    type_sowing = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField(default=0)
    time_unit = models.IntegerField(default=0)
    age = models.PositiveIntegerField(default=0)
    perimeter_closure = models.CharField(max_length=100, blank=True, null=True)
    distance_plants = models.FloatField(default=0)
    distance_rows = models.FloatField(default=0)
    suggestion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Producción Agricola: {}'.format(self.production)

    def save(self, *args, **kwargs):
        """
        calculate length measurement before saving.
        3 -> kilometer (km) = 1000 m
        2 -> hectometer (hm) 100 m
        1 -> decameter (dam) 10 m
        0 -> meter (m) = 1 m

        calculate the age of the plantation before saving.
        2 -> ages (y) = 365 d
        1 -> months (m) = 30 d
        0 -> days (d) = 1 d
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

        if self.time_unit == 0:
            self.age = self.amount*1
        elif self.time_unit == 1:
            self.age = self.amount*30
        elif self.time_unit == 2:
            self.age = self.amount*360
        else:
            return "Time unit no valid"

            # Call the real save() method
        super(ProductionAgricultural, self).save(*args, **kwargs)
