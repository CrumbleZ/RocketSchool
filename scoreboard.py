# libs imports
import cv2
import numpy as np

# custom imports
import colors

"""
This has the objectives of extracting parts of the scoreboard
from a Rocket League screenshot where the "WINNER" message
is already displayed

As this is a work in progress, it is intended to be used
only on 1920x1080 screenshots as selectors are hardcoded
"""


def extract_match_score(frame):
	# Locations and sizes
	x, y, w, h = 600, 290, 65, 310		# zone to extract
	sh = 60								# score_height

	# extract the column where both score appears
	subframe = frame[y: y+h, x:x+w]			# extract score column from scoreboard

	# separate scores
	# TODO : adapt if match is not 3v3,
	# TODO : because score may not be at indicated position

	winner = subframe[0:sh, 0:w]
	loser = subframe[h-sh:h, 0:w]

	# make a mask out of them and dilate them ready
	# for text recognition
	winner = cv2.inRange(winner, colors.team_score_lower_white, colors.team_score_upper_white)
	loser = cv2.inRange(loser, colors.team_score_lower_white, colors.team_score_upper_white)

	kernel = np.ones((3, 3))
	winner = cv2.dilate(winner, kernel, iterations=1)
	loser = cv2.dilate(loser, kernel, iterations=1)

	# return both results in a dictionary
	return{'winner': winner, 'loser': loser}


def extract_players_score(frame):
	x, y, w, h = 1125, 350, 465, 420		# zone to extract

	subframe = frame[y: y+h, x:x+w]

	mask = cv2.inRange(subframe, colors.connected_lower_blue, colors.connected_upper_blue)
	mask += cv2.inRange(subframe, colors.connected_lower_orange, colors.connected_upper_orange)
	mask += cv2.inRange(subframe, colors.disconnected_lower_blue, colors.disconnected_upper_blue)
	mask += cv2.inRange(subframe, colors.disconnected_lower_orange, colors.disconnected_upper_orange)
	mask += cv2.inRange(subframe, colors.player_lower_white, colors.player_upper_white)

	return cv2.dilate(mask, np.ones((2, 2)), iterations=1)





