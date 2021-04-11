from weather.weather import Weather


class Cloudy(Weather):
    def __init__(self):
        super().__init__()
        self.type = "Cloudy"
        self.coefficient = 0.8
