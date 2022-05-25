"""Weather and weather types."""

import random
from abc import ABC


class Weather(ABC):
    """An abstract class of weather."""

    @staticmethod
    def generate_weather():
        """Generate a random type of weather."""
        return random.choice(weathers)


class Cloudy(Weather):
    """Generate a cloudy type of weather."""
    def __init__(self):
        self.type = "Cloudy"
        self.coefficient = 0.8


class PartiallyCloudy(Weather):
    """Generate a partially cloudy type of weather."""
    def __init__(self):
        self.type = "PartiallyCloudy"
        self.coefficient = 1


class Rainy(Weather):
    """Generate a rainy type of weather."""
    def __init__(self):
        self.type = "Rainy"
        self.coefficient = 0.45


class Sunny(Weather):
    """Generate a sunny type of weather."""
    def __init__(self):
        self.type = "Sunny"
        self.coefficient = 0.85


class Storm(Weather):
    """Generate a stormy type of weather."""
    def __init__(self):
        self.type = "Storm"
        self.coefficient = 0.2


weathers = [Cloudy(), PartiallyCloudy(), Rainy(), Sunny(), Storm()]
