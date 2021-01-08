""" Producer Person Model """

# Django
from django.db import models


class ProducerPerson(models.Model):
    """Modelo de datos de personas que componen el grupo familiar
    del productor."""

    producer = models.ForeignKey(
        "producer.Producer",
        related_name='producer_person',
        on_delete=models.CASCADE
        )
    family_relation = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    has_primary_studies = models.BooleanField()
    has_secondary_studies = models.BooleanField()
    has_tertiary_studies = models.BooleanField()
    has_university_studies = models.BooleanField()
    perform_work_activity = models.BooleanField()
    description = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return "{} {}, {}".format(self.first_name, self.last_name, self.family_relation)