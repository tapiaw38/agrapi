""" Production Livestock Sheep Cycle """

from django.db import models


class LivestockSheepCycle(models.Model):
    """ Ciclo ovino de la produccion ganadera """

    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_sheep_cycle",
        on_delete=models.CASCADE
        )
    sheep_under_six_months = models.PositiveIntegerField(default=0)
    sheep_older_six_months_to_calving = models.PositiveIntegerField(default=0)
    sheep_older_six_months_one_year = models.PositiveIntegerField(default=0)
    number_sheep = models.PositiveIntegerField(default=0)
    number_capons = models.PositiveIntegerField(default=0)
    number_rams = models.PositiveIntegerField(default=0)