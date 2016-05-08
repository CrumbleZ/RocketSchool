# Part of the code in extract_players_score() comes from the internet
# Source :
# http://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python
# NB : Values are tweaked to meet our needs

# part of the code adapted from opencv2 to opencv3
# with source : http://stackoverflow.com/questions/32980675/knn-train-in-cv2-with-opencv-3-0

# libs imports
import cv2
import numpy as np

# custom imports
import colors
import classes

"""
This has the objectives of extracting parts of the scoreboard
from a Rocket League screenshot where the "WINNER" message
is already displayed

As this is a work in progress, it is intended to be used
only on 1920x1080 screenshots as selectors are hardcoded
"""

def myround(x, base=20):
    return int(base * round(float(x)/base))


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

	# Get black and white widened text
	mask = cv2.inRange(subframe, colors.connected_lower_blue, colors.connected_upper_blue)
	mask += cv2.inRange(subframe, colors.connected_lower_orange, colors.connected_upper_orange)
	mask += cv2.inRange(subframe, colors.disconnected_lower_blue, colors.disconnected_upper_blue)
	mask += cv2.inRange(subframe, colors.disconnected_lower_orange, colors.disconnected_upper_orange)
	mask += cv2.inRange(subframe, colors.player_lower_white, colors.player_upper_white)

	dilation = cv2.dilate(mask, np.ones((2, 2)), iterations=1)

	# Load trained data and prepare model for extraction
	samples = np.loadtxt('generalsamples.data', np.float32)
	responses = np.loadtxt('generalresponses.data', np.float32)
	responses = responses.reshape((responses.size, 1))

	model = cv2.ml.KNearest_create()
	model.train(samples, cv2.ml.ROW_SAMPLE, responses)

	# Extract data
	# for unknown reason, there's no opencv conversion
	# from hsv to bgr... so let's use the video game trick
	# I call : quick-save quick-load
	cv2.imwrite("./resources/tmp.png", dilation)
	dilation = cv2.imread("./resources/tmp.png")
	out = np.zeros(dilation.shape, np.uint8)
	gray = cv2.cvtColor(dilation , cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

	drop, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	digits = []

	for cnt in contours:
		if cv2.contourArea(cnt) > 100:
			[x, y, w, h] = cv2.boundingRect(cnt)
			if 20 < h < 25 and w < 20:
				cv2.rectangle(dilation, (x, y), (x + w, y + h), (0, 255, 0), 2)
				roi = thresh[y:y + h, x:x + w]
				roismall = cv2.resize(roi, (10, 10))
				roismall = roismall.reshape((1, 100))
				roismall = np.float32(roismall)
				retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
				string = str(int((results[0][0])))

				# group individual digits together to form numbers
				digits.append({'x': myround(x, 10), 'y': myround(y), 'digit': string})
				cv2.putText(out, string, (x, y + h), 0, 1, (0, 255, 0))

	for digit in digits:
		print(digit)

	cv2.imshow('im', dilation)
	cv2.imshow('out', out)

	return out







