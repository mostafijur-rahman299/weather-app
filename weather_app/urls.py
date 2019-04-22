# @Date:   2019-04-21T14:38:18+06:00
# @Last modified time: 2019-04-21T14:39:23+06:00
from django.urls import path
from .views import Weather

urlpatterns = [
    path('', Weather, name='weather')
]
