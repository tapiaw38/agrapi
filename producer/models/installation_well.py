""" Model Installation Well """

from django.db import models


class InstallationWell(models.Model):
    """Pozos de agua dentro de las intalaciones, 
    activo, latitud, longitud"""

    installation = models.ForeignKey(
        "producer.ProductionInstallation",
        related_name="installation_well",
        on_delete=models.CASCADE
        )
    is_active = models.BooleanField()
    lat = models.FloatField()
    lng = models.FloatField()