""" Model Production Installation """

from django.db import models

class ProductionInstallation(models.Model):
    """Instalaciones de la producción"""

    production = models.OneToOneField(
        "producer.Production",
        related_name="production_installation", 
        on_delete=models.CASCADE
        )
    has_windmills = models.BooleanField(default=False)
    has_australian_tanks = models.BooleanField(default=False)
    has_dams = models.BooleanField(default=False)
    has_truck_scale = models.BooleanField(default=False)
    has_fire_break = models.BooleanField(default=False)
    has_minced_steel = models.BooleanField(default=False)
    has_pools = models.BooleanField(default=False)

    def __str__(self):
        return 'Instalaciones de Produccion {}'.format(self.production)
    