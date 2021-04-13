import random

from weather.sunny import Sunny

STADIUM_NAMES = {
    "Camp Nou": 99354,
    "Wembley Stadium": 90000,
    "Signal Iduna Park": 81359,
    "Estadio Santiago Bernabeu": 81044,
    "Luzhniki Stadium": 81006,
    "San Siro": 80018,
    "Stade de France": 80000,
    "Ataturk Olimpiyat Stadium": 76092,
    "Old Trafford": 75811,
    "Allianz Arena": 75000,
    "Olympiastadion": 74648,
    "Millennium Stadium": 74500,
    "Stadio Olimpico": 72698,
    "NSC Olimpiyskiy": 70050,
    "OAKA Stadium": 69918,
    "Baku Olympic Stadium": 68700,
    "Wanda Metropolitano": 68000,
    "Stade Velodrome": 67000,
    "Estadio da Luz": 64400,
    "VELTINS-Arena": 61637,
    "Estadio Benito Villamarin": 60720,
    "Celtic Park": 60500,
    "Mercedes-Benz-Arena": 60441,
    "Emirates Stadium": 60361,
    "Estadio La Cartuja de Sevilla": 60000,
    "London Stadium": 60000,
    "Parc Olympique Lyonnais": 59186,
    "Anfield": 54074,
    "Amsterdam Arena": 53748,
    "St. James Park": 52339
}

class Stadium:
    def __init__(self):
        self.name = None
        self.capacity = None
        self.spectators = 0

    def generate_stadium(self):
        all_stadiums_as_list = list(STADIUM_NAMES.items())
        generated_stadium = random.choice(all_stadiums_as_list)
        self.name = generated_stadium[0]
        self.capacity = generated_stadium[1]

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
            return f"Clouds darkened the skies at {self.name} as {int(self.spectators)} spectators turned up for the match."


s = Stadium()
s.generate_stadium()
s.generate_number_spectators(Sunny())

print(s.name)
print(s.capacity)
print(s.generate_number_spectators(Sunny()))