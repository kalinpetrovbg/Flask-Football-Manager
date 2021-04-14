import random
from awayteam import AWAY_TEAMS
from stadium.stadium import Stadium
from weather.weather_data import WEATHER_TYPES

home_team_name = input('What will be your team\'s name: ')
away_team_name = random.choice(AWAY_TEAMS)

print(f"\n{home_team_name} : {away_team_name}")

stadium = Stadium()
weather = random.choice(WEATHER_TYPES)
stadium.generate_stadium()

print(stadium.generate_number_spectators(weather))




# weather info

# lineups

# schemas

# Start of the Game

# conclusions

# stats