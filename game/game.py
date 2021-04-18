import random
import time

from awayteam import away_team
from hometeam import *
from stadium.stadium import Stadium
from weather.weather_data import WEATHER_TYPES

home_team_name = home_team  # input('What will be your team\'s name: ')
away_team_name = away_team

score_home = 0
score_away = 0

print(f"\n{home_team_name} - {away_team_name} = {score_home} : {score_away}")

time.sleep(1)

stadium = Stadium()
weather = random.choice(WEATHER_TYPES)
stadium.generate_stadium()

print(stadium.generate_number_spectators(weather))

match_time = 0

time.sleep(1)
print("Ref blows the whistle and we're under way!")

for x in range(1, 11):
    number = random.randint(1, 11)
    if number % 2 == 0:
        attacking_team = home_team_name
        score_home += 1
        random_home_scorer = random.choice(home_team_players)
        print(f"{random_home_scorer} scores!")
        time.sleep(2)
    else:
        attacking_team = away_team
        score_away += 1

print(f"\n{home_team_name} - {away_team_name} = {score_home} : {score_away}")

# current_time = 22
#
# LIST_OF_ATTACKS = [
#     f"{home_team_name} broke through on the left {current_time} minutes into the game, with Panikos Moditis firing "
#     f"in from an acute angle to give the home side a {score_home + 1} - {score_away} lead.",
# ]
#
# attack_event = random.choice(LIST_OF_ATTACKS)
# print(attack_event)
# current_time = 47
# attack_event = random.choice(LIST_OF_ATTACKS)
# print(attack_event)



# print(attack(attack_event, attacking_team))


# weather info

# lineups

# schemas

# Start of the Game

# conclusions

# stats