import numpy as np

# Picked HSV Blue
# connected : [103, 138, 254]
# disconnected : [107, 147, 134]
connected_lower_blue = np.array([100, 135, 230])
connected_upper_blue = np.array([105, 140, 255])
disconnected_lower_blue = np.array([100, 130, 120])
disconnected_upper_blue = np.array([115, 165, 150])

# Picked HSV Orange
# connected : [21, 135, 255]
# disconnected : [16, 151, 145]
connected_lower_orange = np.array([15, 130, 230])
connected_upper_orange = np.array([25, 140, 255])
disconnected_lower_orange = np.array([10, 130, 125])
disconnected_upper_orange = np.array([20, 170, 165])

# Picked HSV White
# Player : [0, 0, 255]
player_lower_white = np.array([0, 0, 220])
player_upper_white = np.array([255, 45, 255])

# Picked HSV Team score
# Blue team score : [101  68  30]
# Orange team score : [24 94 27]
team_score_lower_white = np.array([0, 0, 220])
team_score_upper_white = np.array([255, 20, 255])

# Picked HSV Team color-name color
# Blue : [102 141 255]
# Orange : [ 22 143 255]
team_name_lower_blue = np.array([85, 125, 230])
team_name_upper_blue = np.array([115, 160, 255])
team_name_lower_orange = np.array([10, 120, 230])
team_name_upper_orange = np.array([35, 170, 255])

