from abc import ABC


class Weather(ABC):
    pass


class Cloudy(Weather):
    def __init__(self):
        self.type = "Cloudy"
        self.coefficient = 0.8


class PartiallyCloudy(Weather):
    def __init__(self):
        self.type = "PartiallyCloudy"
        self.coefficient = 1


class Rainy(Weather):
    def __init__(self):
        self.type = "Rainy"
        self.coefficient = 0.45


class Sunny(Weather):
    def __init__(self):
        self.type = "Sunny"
        self.coefficient = 0.85


class Storm(Weather):
    def __init__(self):
        self.type = "Storm"
        self.coefficient = 0.2


WEATHER_TYPES = [
    Cloudy(),
    PartiallyCloudy(),
    Rainy(),
    Sunny(),
    Storm()
]
