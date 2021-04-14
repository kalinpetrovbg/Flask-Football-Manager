import random
from awayteam import away_team
from stadium.stadium import Stadium
from weather.weather_data import WEATHER_TYPES

home_team_name = "FC Kalin"  # input('What will be your team\'s name: ')
away_team_name = away_team

print(f"\n{home_team_name} : {away_team_name} = 0:0")

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