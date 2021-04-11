from weather.weather import Weather


class Sunny(Weather):
    def __init__(self):
        super().__init__()
        self.type = "Sunny"
        self.coefficient = 0.85
