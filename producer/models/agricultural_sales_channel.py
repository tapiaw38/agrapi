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
    is_collector = models.BooleanField(default=False)
    is_cooperative = models.BooleanField(default=False)
    is_exporter = models.BooleanField(default=False)
    use_baler = models.BooleanField(default=False)
    use_fair = models.BooleanField(default=False)
    use_industry = models.BooleanField(default=False)
    use_fridge = models.BooleanField(default=False)

    def __str__(self):
        return 'Canal de ventas {}'.format(self.production_agricultural)
    