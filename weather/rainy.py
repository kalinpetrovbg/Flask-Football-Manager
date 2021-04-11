from weather.weather import Weather


class Rainy(Weather):
    def __init__(self):
        super().__init__()
        self.coefficient = 0.45

