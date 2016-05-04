__author__ = "Gabriel Freitas, THomas Roulin"

from PIL import Image
import pytesseract

import cv2
import numpy as np

if __name__ == "__main__":
	frame = cv2.imread("./resources/test_002.jpg")
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# pxb = hsv[466, 740]
	# pxo = hsv[203, 746]
	# pxw = hsv[553, 795]
	# print("blue  : {}".format(pxb))
	# print("orange : {}".format(pxo))
	# print("white : {}".format(pxw))

	lower_blue = np.array([100, 100, 230])
	upper_blue = np.array([105, 170, 255])

	lower_orange = np.array([12, 125, 200])
	upper_orange = np.array([30, 145, 255])

	lower_white = np.array([0, 0, 200])
	upper_white = np.array([30, 30, 255])

	blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
	blue_result = cv2.bitwise_and(frame, frame, mask=blue_mask)

	orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
	orange_result = cv2.bitwise_and(frame, frame, mask=orange_mask)

	white_mask = cv2.inRange(hsv, lower_white, upper_white)
	white_result = cv2.bitwise_and(frame, frame, mask=white_mask)

	total = blue_result + orange_result + white_result
	ret2, total_bw = cv2.threshold(total, 0, 255, cv2.THRESH_BINARY)

	kernel = np.ones((3, 3), np.uint8)

	dilation = cv2.dilate(total_bw, kernel, iterations=1)

	cv2.imshow("TOTAL", dilation)

	# cv2.imshow("BLUE MASK", blue_result)
	cv2.imwrite("./resources/tmp.png", total_bw)
	#
	# cv2.imshow("ORANGE MASK", orange_result)


	image = Image.open("./resources/tmp.png")
	print(pytesseract.image_to_string(image))













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