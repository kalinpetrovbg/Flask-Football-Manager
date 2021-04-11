from weather.weather import Weather


class Rainy(Weather):
    def __init__(self):
        super().__init__()
        self.coefficient = 0.45
    
    def __str__(self):
        return "The wet pitch made it difficult for technical or quick players to stand out. " \
               "For once, the players relying on physical strength gained the upper hand."
