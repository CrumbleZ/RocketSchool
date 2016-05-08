__author__ = "Gabriel Freitas, THomas Roulin"

from PIL import Image
import pytesseract

import cv2
import numpy as np

# custom imports
import colors
import scoreboard
from classes import Player
import match_ranks


if __name__ == "__main__":
    frame = cv2.imread("./resources/endgame/hd_004.png")
    icons = scoreboard.extract_rank_icons(frame)

    cv2.imwrite("./resources/tmp.png", icons)
    posranks = match_ranks.process(icons)

    for pr in posranks:
        cv2.putText(frame, pr.rank.name, (10, pr.pos + 64), 0, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("frame", frame)


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
