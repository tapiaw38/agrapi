"""Main URLs module."""

from django.contrib import admin
from django.urls import path, include
# import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include(('user.urls', 'users'), namespace='users')),
    path('api/v1.0/', include(('producer.urls', 'producers'), namespace='producers')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)