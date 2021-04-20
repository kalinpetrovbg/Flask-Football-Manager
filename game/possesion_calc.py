from awayteam import *
from hometeam import *

possession_home_team = 100 * (HOME_TEAMS.midfield / (HOME_TEAMS.midfield + AWAY_TEAMS.midfield))
possession_away_team = 100 * (AWAY_TEAMS.midfield / (AWAY_TEAMS.midfield + HOME_TEAMS.midfield))