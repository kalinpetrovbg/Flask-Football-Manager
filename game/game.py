import random
import time

from awayteam import away_team
from stadium.stadium import Stadium
from weather.weather_data import WEATHER_TYPES

home_team_name = "FC Kalin"  # input('What will be your team\'s name: ')
away_team_name = away_team

print(f"\n{home_team_name} : {away_team_name} = 0:0")

time.sleep(2)

stadium = Stadium()
weather = random.choice(WEATHER_TYPES)
stadium.generate_stadium()

print(stadium.generate_number_spectators(weather))

match_time = 0
print("Ref blows the whistle and we're under way!")

attack_event = random.choice(list_of_attacks)

def attack(event, team):



print(attack(attack_event, attacking_team))



# weather info

# lineups

# schemas

# Start of the Game

# conclusions

# stats