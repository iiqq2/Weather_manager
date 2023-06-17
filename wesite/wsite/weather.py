from pyowm import OWM
from django.http import HttpResponse
from wsite.models import City


def get_weather(City):
    owm = OWM('ced4a711ff493fc0198799316eb41b5d')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(City).weather
    w = observation.to_dict()
    return w


def update_weather(city_name):
    try:
        city = City.objects.get(name=city_name)
        city.weather_data = get_weather(city_name)
        city.save()
    except City.DoesNotExist:
        return HttpResponse(status=404)