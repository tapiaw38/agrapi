""" Pollster Producer Model """

# Django.
from django.db import models

# Utilities
from utils.models import ProduModel


class Pollster(ProduModel):
    """ Clase Encuestadores de productores. """

    user = models.ForeignKey(
        "user.User",
        related_name="pollsters",
        on_delete=models.CASCADE
        )
    profile = models.ForeignKey(
        "user.Profile",
        on_delete=models.CASCADE
        )
    
    def __str__(self):
        return 'Registro de {}, creado: {}'.format(self.user, str(self.created))
