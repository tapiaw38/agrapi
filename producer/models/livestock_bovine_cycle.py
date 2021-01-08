""" Production Livestock Bovine Cycle """

from django.db import models


class LivestockBovineCycle(models.Model):
    """ Modelo del ciclo bovino de la produccion ganadera """
    
    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_bovine_cycle",
        on_delete=models.CASCADE
        )
    calves_under_one_year = models.PositiveIntegerField(default=0)
    heifers_one_to_two_years = models.PositiveIntegerField(default=0)
    heifers_over_two_years = models.PositiveIntegerField(default=0)
    number_cows = models.PositiveIntegerField(default=0)
    steers_one_to_two_years = models.PositiveIntegerField(default=0)
    steers_older_two_years = models.PositiveIntegerField(default=0)
    bulls_one_to_two_years = models.PositiveIntegerField(default=0)
    bulls_older_two_years = models.PositiveIntegerField(default=0)
    number_oxen_torunos = models.PositiveIntegerField(default=0)


