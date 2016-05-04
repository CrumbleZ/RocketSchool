import cv2
import numpy as np
from copy import copy

# CONSTS
SB_WIDTH = 1500
SB_HEIGHT = 700


# CLASSES
class RocketUtils:
    SKILL_TIER_COUNT = 16
    SKILL_TIER_PATH = 'resources/SkillTierIcons/Icon_SkillGroup{}.png'

    @staticmethod
    def templates_path():
        return [RocketUtils.SKILL_TIER_PATH.format(i) for i in range(RocketUtils.SKILL_TIER_COUNT)]


# MAIN
sb_path = 'scoreboards/scoreboard0.png'
sb_img_raw = cv2.imread(sb_path)
# sb_img = cv2.resize(sb_img_raw, (SB_WIDTH, SB_HEIGHT), interpolation=cv2.INTER_CUBIC)[0:700, 0:200]
sb_img = copy(sb_img_raw)

img_b, img_g, img_r = cv2.split(sb_img)

channels = [img_b, img_g, img_r]
imgs = [copy(sb_img) for i in range(3)]

for path in RocketUtils.templates_path():

    template = cv2.imread(path, 0)
    w, h = template.shape[::-1]

    for i in range(len(channels)):
        res = cv2.matchTemplate(channels[i], template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)
        print(loc)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(imgs[i], pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

for i in range(len(imgs)):
    cv2.imshow("{}".format(i), imgs[i])
cv2.waitKey(0)
