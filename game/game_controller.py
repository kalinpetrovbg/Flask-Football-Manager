from game.awayteam import AwayTeam
from game.hometeam import HomeTeam


class Game:
    def __init__(self, home_team: HomeTeam, away_team: AwayTeam):
        self.home_team = home_team
        self.away_team = away_team
        self.date = None
        self.result = None

    def intro(self):
        pass

    def starting_lineup(self):
        result = f"The following players took the field for {self.home_team}: \n"
        result += f"{self.away_team}'s lineup was: "