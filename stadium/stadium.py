"""Build the stadium from a dict with random real stadiums."""
import random

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
    "St. James Park": 52339,
}


class Stadium:
    """Build the stadium properies."""

    name = None
    spectators = 0
    capacity = None

    def __str__(self):
        return f'Stadium "{Stadium.name}" with {self.capacity} capacity.'

    @staticmethod
    def generate_stadium():
        """Create a random stadium class."""

        generated_stadium = random.choice(list(STADIUM_NAMES.items()))
        Stadium.name, Stadium.capacity = generated_stadium
        return Stadium

    @staticmethod
    def generate_visitors(weather):
        """Generate the number of visitors based on the weather conditions."""

        Stadium.spectators = Stadium.capacity * weather.coefficient
        return Stadium.spectators

    @staticmethod
    def generate_message(weather):
        """Generate different intro message based on the weather conditions."""

        if weather.type == "Rainy":
            return (
                f"It had rained all day, but {int(Stadium.spectators)} hardy fans still made it out "
                f'to "{Stadium.name}".'
            )
        elif weather.type == "Sunny":
            return (
                f"It was an exceptionally hot day for the crowd of {int(Stadium.spectators)} that came out"
                f' to "{Stadium.name}".'
            )
        elif weather.type == "PartiallyCloudy":
            return (
                f'{int(Stadium.spectators)} spectators arrived at "{Stadium.name}",'
                f"where weather conditions were pretty good for football."
            )
        elif weather.type == "Cloudy":
            return (
                f'Clouds darkened the skies at "{Stadium.name}" as {int(Stadium.spectators)} '
                f"spectators turned up for the match."
            )
        elif weather.type == "Storm":
            return (
                f'The storm has almost emptied "{Stadium.name}" but there are still {int(Stadium.spectators)} '
                f"enthusiasts today."
            )
