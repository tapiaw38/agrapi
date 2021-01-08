""" Producer URLs"""

# Django
from django.urls import path, re_path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views 
from .views import producer as polls_views

#from .viewsets import LocationList


router = DefaultRouter()
router.register(r'producers', polls_views.PollsterViewSet, basename='producers')
router.register('productive/data', polls_views.ProductiveDataViewSet, basename='productive_data')


urlpatterns = [
    #re_path(r'^createProduction/(?P<producer>.+)/$', CreateProduction.as_view(), name='createProduction'),
]+ router.urls