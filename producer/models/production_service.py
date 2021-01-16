""" Production Service """

from django.db import models

AQUA_CHOICES=(
    ("Red","Red"),
    ("Perforación","Perforación"),
    ("Pozo","Pozo"),
    ("Cisterna","Cisterna"),
    ("Canal","Canal"),
    ("Arrollo","Arrollo"),
    ("Acuifero","Acuifero"),
)

class ProductionService(models.Model):
    """Servicios del emprendimiento,
    tipo de luz y agua, generadores,
    paneles solares."""

    production = models.OneToOneField(
        "producer.Production",
        related_name="production_service",
        on_delete=models.CASCADE
        )
    has_service_aqua = models.BooleanField(default=False) 
    type_service_aqua = models.CharField(max_length=30, blank=True, null=True)
    has_service_energy = models.BooleanField(default=False)
    type_service_energy = models.CharField(max_length=100, blank=True, null=True)
    has_rural_energy = models.BooleanField(default=False)
    has_generator = models.BooleanField(default=False)
    has_hydraulic_generator = models.BooleanField(default=False)
    has_solar_panels = models.BooleanField(default=False)

    def __str__(self):
        return 'Servicios de Producción {}'.format(self.production.producer)