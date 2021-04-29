from django.db import models
""" Producer Model """

# Django
from django.core.validators import RegexValidator
# utilities
from utils.models import ProduModel

GENDER_CHOICES = (
    ('Hombre', 'Hombre'),
    ('Mujer', 'Mujer'),
)


class Producer(ProduModel):
    """Modelo de datos personales del productor."""
    pollster = models.OneToOneField(
        "producer.Pollster",
        related_name="producer",
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    gender = models.CharField(max_length=10)

    document_regex = RegexValidator(
        regex=r'\d{8,8}$',
        message="Debes ingresar un número de DNI sin puntos."
    )
    document = models.CharField(validators=[document_regex], max_length=8)

    phone_regex = RegexValidator(
        regex=r'\d{10,10}$',
        message="Debes ingresar un número con el siguiente formato: 3837430000. Hasta 10 digitos."
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10, blank=True, null=True)
    another_phone_number = models.CharField(
        validators=[phone_regex], max_length=10, blank=True, null=True)

    email = models.EmailField(
        'email addres',
        unique=True,
        error_messages={
            'unique': 'There is already a user with this email.',
        }
    )

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)
