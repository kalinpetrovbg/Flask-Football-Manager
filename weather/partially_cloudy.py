from weather.weather import Weather


class PartiallyCloudy(Weather):
    def __init__(self):
        super().__init__()
        self.type = "PartiallyCloudy"
        self.coefficient = 1
