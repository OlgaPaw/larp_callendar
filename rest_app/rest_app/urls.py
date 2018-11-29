from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static

from rest_app import settings
from larp_calendar.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.BASE_DIR)
