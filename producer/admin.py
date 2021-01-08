# Django
from django.contrib import admin

# Models
from producer.models import (
    Pollster,
    Producer,
    ProducerHome,
    ProducerPerson,
    ProducerVehicle,
    Production,
) 
# Register your models here.


# Register Models Related Producer 
admin.site.register(Pollster)
admin.site.register(Producer)

"""
admin.site.register(ProducerHome)
admin.site.register(ProducerPerson)
admin.site.register(ProducerVehicle)

# Register Models Related Producer 
admin.site.register(Production)

admin.site.register(Production)
admin.site.register(Activity)
admin.site.register(Worker)
admin.site.register(Services)
#Register type production
admin.site.register(ProductionAgricultural)
admin.site.register(AgriculturalActivity)
admin.site.register(ProductionLivestock)
admin.site.register(LivestockActivity)
admin.site.register(Agroindustry)
"""