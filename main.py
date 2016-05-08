__author__ = "Gabriel Freitas, THomas Roulin"

from PIL import Image
import pytesseract

import cv2
import numpy as np

#custom imports
import colors
import scoreboard

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
	return image[y: y+h, x:x+w]


if __name__ == "__main__":
	frame = cv2.imread("./resources/endgame/hd_001.png")
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# acces with "winner" or "loser" keywords
	# match_score = scoreboard.extract_match_score(hsv)
	# cv2.imshow("winner", match_score["winner"])
	# cv2.imshow("loser", match_score["loser"])

	# player score
	player_score = scoreboard.extract_players_score(hsv)
	cv2.imshow("out", player_score)



	# hsv = select_zone(hsv, X, Y, W, H)
	#
	# blue_mask = get_blue_mask(hsv)
	# orange_mask = get_orange_mask(hsv)
	# player_mask = get_player_mask(hsv)
	#
	# cv2.imshow("blue mask", blue_mask)
	# element = cv2.getStructuringElement(cv2.MORPH_RECT, (10,1))
	# erosion = cv2.erode(blue_mask, element, iterations=1)
	# cv2.imshow("eroded", erosion)
	#
	#
	#
	# total_mask = blue_mask + orange_mask + player_mask
	#
	# element = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
	# erosion = cv2.erode(total_mask, element, iterations=1)

	# image = Image.open("./resources/tmp.png")
	# print(pytesseract.image_to_string(image))













	# #cv2.imshow("original", image)
	#
	# #Tries to detach the black border of the scoreboard
	# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# inverse_gray = 255 - image_gray
	# #cv2.imshow("reverse gray", inverse_gray)
	# #cv2.imshow("GRAY", image_gray)
	# ret, lower = cv2.threshold(image_gray, 10, 255, 0)
	# ret, upper = cv2.threshold(image_gray, 20, 255, 0)
	# ret, random = cv2.threshold(image_gray, 10, 255, 0)
	# #cv2.imshow("RAND", upper)
	# #extracted_border = cv2.bitwise_xor(lower, upper)
	# extracted_border = lower - upper
	# extracted_border = cv2.bitwise_xor(lower, extracted_border)
	# extracted_border = 255 - extracted_border
	#
	# cv2.imshow("RESULT", extracted_border)
	#
	# ##Find lines that determines the scoreboard
	# # edges = cv2.Canny(extracted_border, 50, 100, apertureSize = 3)
	# # cv2.imshow("EDGES", edges)
	#
	# lines = cv2.HoughLines(extracted_border, 30, numpy.pi / 2, 20)
	#
	# for line in lines:
	# 	for rho, theta in line:
	# 		a = numpy.cos(theta)
	# 		b = numpy.sin(theta)
	# 		x0 = a*rho
	# 		y0 = b*rho
	# 		x1 = int(x0 + 2000*(-b))
	# 		y1 = int(y0 + 2000*(a))
	# 		x2 = int(x0 - 2000*(-b))
	# 		y2 = int(y0 - 2000*(a))
	#
	# 		cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
	#
	# cv2.imwrite('Hello.jpg', image)

	cv2.waitKey(0)