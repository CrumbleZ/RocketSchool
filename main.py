__author__ = "Gabriel Freitas, THomas Roulin"

from PIL import Image
import pytesseract

import cv2
import numpy as np

# custom imports
import colors
import scoreboard
from classes import Player

X = 580
W = 1720 - X
Y = 270
H = 810 - 270


def get_blue_team_score_mask(frame):
    return cv2.inRange(frame, colors.team_score_lower_blue, colors.team_score_upper_blue)


def get_blue_mask(hsvimage):
    connected_blue_mask = cv2.inRange(hsvimage, colors.connected_lower_blue, colors.connected_upper_blue)
    disconnected_blue_mask = cv2.inRange(hsvimage, colors.disconnected_lower_blue, colors.disconnected_upper_blue)
    return connected_blue_mask + disconnected_blue_mask


def get_orange_mask(hsvimage):
    connected_orange_mask = cv2.inRange(hsvimage, colors.connected_lower_orange, colors.connected_upper_orange)
    disconnected_orange_mask = cv2.inRange(hsvimage, colors.disconnected_lower_orange, colors.disconnected_upper_orange)
    return connected_orange_mask + disconnected_orange_mask


def get_player_mask(hsvimage):
    return cv2.inRange(hsvimage, colors.player_lower_white, colors.player_upper_white)


def select_zone(image, x, y, w, h):
    return image[y: y + h, x:x + w]


if __name__ == "__main__":
    frame = cv2.imread("./resources/endgame/hd_003.png")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # acces with "winner" or "loser" keywords
    # match_score = scoreboard.extract_match_score(hsv)
    # cv2.imshow("winner", match_score["winner"])
    # cv2.imshow("loser", match_score["loser"])

    # player score
    # players = scoreboard.extract_players_score(hsv)
    # print(players[0].name)

    winner = scoreboard.determine_winning_team(hsv)[0]
    print(winner)

    cv2.waitKey(0)
