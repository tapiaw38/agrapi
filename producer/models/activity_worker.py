""" Model Worker Activity of Activity Producer """

# Django
from django.db import models

GENDER_CHOICES = (
    ('Hombre','Hombre'),
    ('Mujer','Mujer'),
)

WORKER_CHOICES = (
    ('Trabajador','Trabajador'),
    ('Familiar','Familiar')
)

JOB_CHOICES = (
    ('Residente','Residente'),
    ('Permanente','Permanente'),
    ('Transitorio','Transitorio')
) 

class ActivityWorker(models.Model):
    '''Modelo de trabajadores relacionados 
    con la actividad laboral'''

    activity = models.ForeignKey(
        "producer.ProducerActivity",
        related_name="activity_worker",
        on_delete=models.CASCADE
        )
    is_formal_worker = models.BooleanField()
    type_person = models.CharField(max_length=50)
    is_resident = models.BooleanField()
    gender = models.CharField(max_length=10)
    receive_remuneration = models.BooleanField()
    work_position = models.CharField(max_length=50)
    type_job = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.work_position, self.type_person)