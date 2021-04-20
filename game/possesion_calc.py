from awayteam import *
from hometeam import *

def calculate_home_team_possession(home_team_mid, away_team_mid):
    return 100 * (home_team_mid / (home_team_mid + away_team_mid))

def calculate_away_team_possession(home_team_mid, away_team_mid):
    return 100 * (away_team_mid / (away_team_mid + home_team_mid))


possession_home_team = calculate_home_team_possession(HOME_TEAMS.midfield, AWAY_TEAMS.midfield)
possession_away_team = calculate_away_team_possession(HOME_TEAMS.midfield, AWAY_TEAMS.midfield)