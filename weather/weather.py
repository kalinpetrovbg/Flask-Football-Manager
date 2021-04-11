from abc import ABC


class Weather(ABC):
    def __init__(self):
        self.type = None
        self.coefficient = 0
