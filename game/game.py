from stadium.stadium import Stadium
import random
from game.awayteam import *
from weather.cloudy import Cloudy
from weather.partially_cloudy import PartiallyCloudy
from weather.rainy import Rainy
from weather.sunny import Sunny

# home_team_name = input('What will be your team\'s name: ')
# away_team_name = random.choice(away_teams_list)
stadium = Stadium()
weather = random.choice([Sunny(), Rainy(), Cloudy(), PartiallyCloudy()])
stadium.generate_stadium()

print(stadium.capacity)




# weather info

# lineups

# schemas

# Start of the Game

# conclusions

# stats