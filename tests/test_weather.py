"""Unit tests for weather folder."""

from weather.weather import Weather


def test_random_weather_choice():
    wea = Weather()

    current_weather = wea.generate_weather()

    assert current_weather.type == "Rainy" \
           or current_weather.type == "Cloudy" \
           or current_weather.type == "PartiallyCloudy" \
           or current_weather.type == "Sunny" \
           or current_weather.type == "Stormy"