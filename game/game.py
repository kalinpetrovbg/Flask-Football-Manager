import random
import time

from stadium.stadium import Stadium
from weather.weather_data import WEATHER_TYPES
from possesion_calc import *
from attack_calc import *

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

    time.sleep(2)
    home_att = number_home_attacks
    away_att = number_away_attacks
    chance_to_attack = random.choice([HOME_TEAMS, AWAY_TEAMS])
    print(chance_to_attack)

    if chance_to_attack == HOME_TEAMS:
        if home_att > 0:
            attacking_team = HOME_TEAMS
            home_att -= 1
            score_home += 1
            random_home_scorer = random.choice(home_team_players)
            print(f"{random_home_scorer} scores!")
        else:
            print(f"{home_team_name} misses a chance to score!")
    elif chance_to_attack == AWAY_TEAMS:
        if away_att > 0:
            attacking_team = AWAY_TEAMS
            away_att -= 1
            score_away += 1
            random_away_scorer = random.choice(away_team_players)
            print(f"{random_away_scorer} scores!")
        else:
            print(f"{away_team_name} misses a chance to score!")


print(f"\n{home_team_name} - {away_team_name} = {score_home} : {score_away}")

print(f"Ball Possession was: {home_team_name} {int(possession_home_team)}% / {away_team_name} {int(possession_away_team)}%")
print(f"Home team did {number_home_attacks} attacks")
print(f"Away team did {number_away_attacks} attacks")



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