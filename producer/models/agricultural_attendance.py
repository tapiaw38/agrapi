""" Production Agricultural Attendance """

from django.db import models



class AgriculturalAttendance(models.Model):
    """ Modelo de cuidados de la actividad """

    production_agricultural = models.OneToOneField(
        "producer.ProductionAgricultural",
        related_name="agricultural_attendance",
        on_delete=models.CASCADE
        )
    use_fertilizers = models.BooleanField(default=False)
    use_food_organic = models.BooleanField(default=False)
    use_pheromones = models.BooleanField(default=False)
    use_hail_mesh = models.BooleanField(default=False)
    make_frost_control = models.BooleanField(default=False)
    other_practices = models.CharField(max_length=40, blank=True, null=True)