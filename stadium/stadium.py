class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.spectators = 0

    def generate_stadium(self):
        pass

    def generate_number_spectators(self, weather):
        self.spectators = self.capacity * weather.coefficient

        if weather.type == "Rainy":
            return 	f"It had rained all day, but {self.spectators} hardy fans still made it out to {self.name}."
        elif weather.type == "Sunny":
            return f"It was an exceptionally hot day for the crowd of {self.spectators} that came out to {self.name}"
        elif weather.type == "PartiallyCloudy":
            return f"{self.spectators} spectators arrived at {self.name}, where weather conditions were pretty" \
                   f" good for football."
        elif weather.type == "Cloudy":
            return f"Clouds darkened the skies at {self.name} as {self.spectators} spectators turned up for the match."
