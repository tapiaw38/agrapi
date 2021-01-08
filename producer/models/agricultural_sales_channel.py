""" Model Sales Channel Production Agricultural """

from django.db import models


class AgriculturalSalesChannel(models.Model):
    """ Modelo canal de ventas 
    relacionado con la produccion """

    production_agricultural = models.OneToOneField(
        "producer.ProductionAgricultural",
        related_name="agricultural_sales_channel",
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
        return 'Canal de ventas {}'.format(self.production_agricultural)
    