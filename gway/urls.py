from api.router import router

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [

    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('contact/', include('contact.urls')),
    path('events/', include('events.urls')),
    path('location/', TemplateView.as_view(
                      template_name='location/index.html'), name='location'),
    path('sermons/', include('sermons.urls')),
    path('subscribe/', include('subscribe.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
