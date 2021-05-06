from hometeam import *
from awayteam import *
from game.game import score_home
from game.game import score_away

winner = HOME_TEAMS.name
loser = AWAY_TEAM.name
scorer = "A"
defender = "B"
passer = "C"
minutes = 0
score = f"{score_home} : {score_away}"

LIST_OF_ATTACKS = [
    f"The bleachers were silenced after {minutes} minutes when {winner}'s {scorer} put the guests "
    f"ahead {score}, following an attack on the right.",

    f"After {minutes} minutes a combination in the middle resulted in a through ball for {scorer} who "
    f"increased {winner}'s lead to {score}.",

    f"The home side put themselves ahead {score} after {minutes} minutes of hard work with a breakthrough from "
    f"{scorer}, who, all by his lonesome, came out of the right wing and hooked the ball over the visitors' keeper.",

    f"{winner} solidified their lead at the {minutes} minute mark, as {scorer} snaked the ball "
    f"through the central line of defense and finished for {score}.",

    f"Cheers filled the stadium as {scorer} broke through the visitors' central defense "
    f"to put away the {score} goal for {winner}.",

    f"The unexpected cross from {winner}'s {passer} opened up the defense and was "
    f"received by {scorer} who finished it off for {score}.",

    f"The counter-attacks of {winner} were deadly and {minutes} minutes into the game, {scorer} "
    f"controlled a long pass from the right flank and finished to make it {score}.",

]