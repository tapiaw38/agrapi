""" Production Property """

# Django
from django.db import models

TENURE_CHOICES = (
    ('Propietario','Propietario'),
    ('Arriendatario','Arriendatario'),
    ('Mediero','Mediero')

)

class ProductionProperty(models.Model):
    """ Modelo de la propiedad y 
    titulos de la produccion """

    production = models.OneToOneField(
        "producer.Production",
        related_name="production_property",
        on_delete=models.CASCADE
        )
    
    land_tenure = models.CharField(max_length=30)
    has_land_title = models.BooleanField()
    cadastre_registration = models.CharField(max_length=30,blank=True, null=True)
    starting_number = models.CharField(max_length=30,blank=True, null=True)