import cv2
import numpy as np
from copy import copy
from classes import *


# ==================================================#
#                     UTILS                        #
# ==================================================#
def remove_same(coords):
    coords.sort(key=lambda x: x.pos)
    i = 1
    while i < len(coords):
        if coords[i].pos - coords[i - 1].pos < 64:
            coords.pop(i)
        else:
            i += 1


class PosRank:
    def __init__(self, pos, rank):
        self.pos = pos
        self.rank = rank


# ==================================================#
#                     CONSTANTS                    #
# ==================================================#
SB_WIDTH = 1500
SB_HEIGHT = 700


# ==================================================#
#                      CORE                         #
# ==================================================#
def main(scoreboard_image_cropped):
    # Cause short name easier
    sb_img = scoreboard_image_cropped

    # Working on every grayscale channel
    img_b, img_g, img_r = cv2.split(sb_img)

    channels = [img_b, img_g, img_r]

    posranks = []
    for r in ranks:
        path = 'resources/SkillTierIcons/Icon_SkillGroup{}.png'.format(r.level)
        template = cv2.imread(path, 0)
        w, h = template.shape[::-1]
        for i in range(len(channels)):
            res = cv2.matchTemplate(channels[i], template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.7
            loc = np.where(res >= threshold)
            posranks += [PosRank(pt[1], r) for pt in zip(*loc[::-1])]

    remove_same(posranks)

    return posranks

    # font = cv2.FONT_HERSHEY_SIMPLEX
    # for pr in posranks:
    #     cv2.putText(sb_img, pr.rank.name, (10, pr.pos + 64), font, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
    #     print(pr.rank.name)
    #     print(pr.pos)
    #
    # cv2.imshow("Scoreboard", sb_img)
    # cv2.waitKey(0)
