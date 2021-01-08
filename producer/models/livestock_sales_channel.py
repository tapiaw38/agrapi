""" Model Sales Channel Production Livestock """

from django.db import models


class LivestockSalesChannel(models.Model):
    """ Modelo canal de ventas 
    relacionado con la produccion """

    production_livestock = models.OneToOneField(
        "producer.ProductionLivestock",
        related_name="livestock_sales_channel",
        on_delete=models.CASCADE
        )
    is_collector = models.BooleanField()
    is_cooperative = models.BooleanField()
    is_exporter = models.BooleanField()
    use_baler = models.BooleanField()
    use_fair = models.BooleanField()
    use_industry = models.BooleanField()
    use_fridge = models.BooleanField()

    def __str__(self):
        return 'Canal de ventas {}'.format(self.production_livestock)