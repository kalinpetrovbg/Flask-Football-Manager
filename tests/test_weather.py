"""Unit tests for weather folder."""

from weather.weather import Weather


def test_random_weather_choice():
    wea = Weather()

    current_weather = wea.generate_weather()

    assert current_weather.type == "Rainy" or "Cloudy" or "Partiallycloudy" or "Sinny" or "Stormy"
