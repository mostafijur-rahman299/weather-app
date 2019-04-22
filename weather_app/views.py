# @Date:   2019-04-21T14:32:45+06:00
# @Last modified time: 2019-04-21T15:46:01+06:00
import requests
from django.shortcuts import render
from .forms import CityForm
from django.http import HttpResponse

def Weather(request):
    # if request.method == 'POST':
    #     form = CityForm(request.POST)
    #     form.save()

    city_name = request.POST.get('name')
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid=6eaf098f9f4aaa97be6c9d2bce94b83d'
        json_data = requests.get(url).json()
        form = CityForm()
        context = {
            'form': form,
            'city': city_name,
            'description': json_data['weather'][0]['description'],
            'icon': json_data['weather'][0]['icon'],
            'temperature': json_data['main']['temp'],
            'humidity': json_data['main']['humidity']
        }
    except:
        return HttpResponse('This city is not add our database!')
    return render(request, 'weather_app/weather.html', context)
