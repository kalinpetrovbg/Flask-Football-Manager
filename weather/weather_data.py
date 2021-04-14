from weather.cloudy import Cloudy
from weather.partially_cloudy import PartiallyCloudy
from weather.rainy import Rainy
from weather.sunny import Sunny

WEATHER_TYPES = [
    Cloudy(),
    PartiallyCloudy(),
    Rainy(),
    Sunny(),
]