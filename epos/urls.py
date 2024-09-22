
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('Basics/',include('Basics.urls')),
        path('Admin/',include('Admin.urls')),
        path('',include('Guest.urls')),
        path('ShopManager/',include('ShopManager.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)