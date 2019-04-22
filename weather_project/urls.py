# @Date:   2019-04-21T14:31:59+06:00
# @Last modified time: 2019-04-21T14:38:07+06:00



"""weather_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls'))
]

if settings.DEBUG:
    urlpatterns += \
            static(settings.STATIC_URL, docuemt_root = settings.STATIC_ROOT)
    urlpatterns += \
            static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
