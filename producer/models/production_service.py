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
    has_service_aqua = models.BooleanField() 
    type_service_aqua = models.CharField(max_length=30)
    has_service_energy = models.BooleanField()
    type_service_energy = models.CharField(max_length=100)
    has_rural_energy = models.BooleanField()
    has_generator = models.BooleanField()
    has_hydraulic_generator = models.BooleanField()
    has_solar_panels = models.BooleanField()

    def __str__(self):
        return 'Servicios de Producción {}'.format(self.production.producer)