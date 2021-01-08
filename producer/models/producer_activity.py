""" Model Producer Activity """

# Django
from django.db import models

CATEGORY_CHOICES = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
    ('E','E'),
    ('F','F'),
    ('G','G'),
    ('H','H'),
    ('I','I'),
    ('J','J'),
    ('K','K'),
)

class ProducerActivity(models.Model):
    """ Modelo de datos de actividad laboral del productor, 
    dependencia, monotributo, categoria personas a cargo."""

    producer = models.OneToOneField(
        "producer.Producer",
        related_name="producer_activity",
        on_delete=models.CASCADE
        )
    works_under_dependency = models.BooleanField()
    is_monotributista = models.BooleanField()
    category = models.CharField(
        blank=True, null=True, max_length=2
        )
    use_external_labor = models.BooleanField(
        help_text="Contrata mano de obra externa para s emprendimiento"
        )

    def __str__(self):
        return 'Actividad laboral productor {}'.format(self.producer)