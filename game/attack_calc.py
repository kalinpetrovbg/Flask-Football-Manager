from awayteam import *
from hometeam import *
from possesion_calc import *

def calculate_home_attacks_number(home_possession):
    if 50 <= home_possession < 54:
        return 5
    if 54 <= home_possession < 57:
        return 6
    if 57 <= home_possession < 62:
        return 7
    if 62 <= home_possession < 65:
        return 8
    if 65 <= home_possession < 70:
        return 9
    if home_possession >= 71:
        return 10

def calculate_away_attacks_number(home_attacks):
    return 10 - home_attacks

number_home_attacks = calculate_home_attacks_number(possession_home_team)
number_away_attacks = calculate_away_attacks_number(number_home_attacks)