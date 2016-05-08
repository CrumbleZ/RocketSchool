__author__ = "Gabriel Freitas, THomas Roulin"

from PIL import Image
import pytesseract

import cv2
import numpy as np
import sys

# custom imports
import colors
import scoreboard
from classes import *
import match_ranks


if __name__ == "__main__":
    # read the frame
    frame = cv2.imread(sys.argv[1])

    # use hsv frame needed for some functions
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # grab a list of players and their scores
    players = scoreboard.extract_players_score(hsv_frame)

    # now that we have players, make a team
    winner, loser = scoreboard.determine_winning_team(hsv_frame)
    team_winner = Team(winner, players[0:len(players) / 2])
    team_loser = Team(loser, players[len(players) / 2:len(players)])

    # extract ranks and associate them to players
    icons = scoreboard.extract_rank_icons(frame)
    posranks = match_ranks.process(icons)

    for pr in posranks:
        index = scoreboard.myround(pr.pos, 64) / 64

        modulo = len(players) / 2

        if(index < modulo):      # winning team
            team_winner.players[index % modulo].rank = pr.rank
        else:               # losing team
            team_loser.players[index % modulo].rank = pr.rank

    # now that we have a both teams, create a game
    game = Game(team_winner, team_loser)


    game.show()

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # acces with "winner" or "loser" keywords
    # match_score = scoreboard.extract_match_score(hsv)
    # cv2.imshow("winner", match_score["winner"])
    # cv2.imshow("loser", match_score["loser"])

    # player score
    # players = scoreboard.extract_players_score(hsv)
    # print(players[0].name)

    # winner = scoreboard.determine_winning_team(hsv)[0]
    # print(winner)

    cv2.waitKey(0)
