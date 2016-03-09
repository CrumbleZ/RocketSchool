import cv2
import numpy as np


# CLASSES
class RocketUtils:
    SKILL_TIER_COUNT = 16
    SKILL_TIER_PATH = 'resources/SkillTierIcons/Icon_SkillGroup{}.png'

    @staticmethod
    def templates_path():
        return [RocketUtils.SKILL_TIER_PATH.format(i) for i in range(RocketUtils.SKILL_TIER_COUNT)]


# MAIN
img_rgb = cv2.imread('scoreboards/scoreboard.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

for path in RocketUtils.templates_path():
    print("Skill tier : {}".format(path))
    template = cv2.imread(path, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('Thank you Corey', img_rgb)
cv2.waitKey(0)
