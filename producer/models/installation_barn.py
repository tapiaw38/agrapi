""" Installation Barn Production """

from django.db import models


class InstallationBarn(models.Model):
    """ Galpon dentro de la instalacion, 
    superficie, latitud, longitud"""

    installation = models.ForeignKey(
        "producer.ProductionInstallation",
        related_name="installation_barn",
        on_delete=models.CASCADE
    )
    height = models.FloatField(default=0)
    width = models.FloatField(default=0)
    surface = models.FloatField(default=0)
    lat = models.FloatField()
    lng = models.FloatField()

    def save(self, *args, **kwargs):
        self.surface = self.width * self.height

        super(InstallationBarn, self).save(
            *args, **kwargs)  # Call the real save() method
