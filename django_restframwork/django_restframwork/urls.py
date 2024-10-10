from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(oauth2_urls, namespace='oauth2_provider')),
    path('', include('book.urls')),
    path('user/', include('user.urls')),
]
