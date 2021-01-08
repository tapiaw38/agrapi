""" Model Production Installation """

from django.db import models

class ProductionInstallation(models.Model):
    """Instalaciones de la producción"""

    production = models.OneToOneField(
        "producer.Production",
        related_name="production_installation", 
        on_delete=models.CASCADE
        )
    has_windmills = models.BooleanField()
    has_australian_tanks = models.BooleanField()
    has_dams = models.BooleanField()
    has_truck_scale = models.BooleanField()
    has_fire_break = models.BooleanField()
    has_minced_steel = models.BooleanField()
    has_pools = models.BooleanField()

    def __str__(self):
        return 'Instalaciones de Produccion {}'.format(self.production)
    