""" Model Sales Channel Production Livestock """

from django.db import models


class LivestockSalesChannel(models.Model):
    """ Modelo canal de ventas 
    relacionado con la produccion """

    livestock_marketing = models.OneToOneField(
        "producer.LivestockMarketing",
        related_name="livestock_sales_channel",
        on_delete=models.CASCADE
        )
    is_collector = models.BooleanField(default=False)
    is_cooperative = models.BooleanField(default=False)
    is_exporter = models.BooleanField(default=False)
    use_baler = models.BooleanField(default=False)
    use_fair = models.BooleanField(default=False)
    use_industry = models.BooleanField(default=False)
    use_fridge = models.BooleanField(default=False)
    make_direct_sale = models.BooleanField(default=False)

    def __str__(self):
        return 'Canal de ventas {}'.format(self.livestock_marketing)