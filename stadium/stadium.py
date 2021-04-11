STADIUM_NAMES = {
    "Camp Nou": 99354,
    "Wembley Stadium": 90000,
    "Croke Park": 82300,
    "Twickenham Stadium": 82000,
    "Signal Iduna Park": 81359,
                                        # Todo  add at least 30 stadiums
}


class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.spectators = 0

    def generate_stadium(self):
        pass

    def generate_number_spectators(self, weather):
        self.spectators = self.capacity * weather.coefficient

        # if it is rainy:
        return 	f"It had rained all day, but {self.spectators} hardy fans still made it out to {self.name}."

