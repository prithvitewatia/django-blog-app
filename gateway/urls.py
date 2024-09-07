from django.conf.urls.static import static
from django.urls import path

from .views import gateway
from django.conf import settings

urlpatterns = [
    path('', gateway, name='gateway'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)