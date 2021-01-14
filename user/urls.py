"""User URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import user as user_views

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
router.register(r'pollsters',user_views.ListUserViewSet, basename='pollsters')

urlpatterns = [
    #path('', include(router.urls))
]+ router.urls

