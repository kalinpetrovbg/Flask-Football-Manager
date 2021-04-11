from game.awayteam import AwayTeam
from game.hometeam import HomeTeam


class Game:
    pass

    @staticmethod
    def starting_lineup(home_team: HomeTeam, away_team: AwayTeam):
        result = f"The following players took the field for {home_team}: \n"
        result += f"{away_team}'s lineup was: "