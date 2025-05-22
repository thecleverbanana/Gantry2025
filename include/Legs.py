# Complete translation from C++ to Python
# IMPORTANT: The following servo ID designation is from the previous
# code, please change them to the new ones we designated (ID number
# sticked onto the side of each servo

import sys
import os
# sys.path.append('/Users/simonto/Library/Mobile Documents/com~apple~CloudDocs/USC Undergraduate/RoboLAND Summer Research/github_repo_jetbrains/')


# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.abspath(__file__))

# Getting the parent directory name
# where the current directory is .
parent = os.path.dirname(current)

grandparent = os.path.dirname(parent)

greatgrandparent = os.path.dirname(grandparent)

# adding the parent directory to
# the sys.path.
sys.path.append(greatgrandparent)



# import servo_control_testing.src.lss as lss
from lss import LSS

R_LEAD_LEG_ID = 0
L_LEAD_LEG_ID = 1
L_HIND_LEG_ID = 2
R_HIND_LEG_ID = 3

BROADCAST_ID = 254

# Initializing LSS classes for each leg
R_LEAD_LEG = LSS(R_LEAD_LEG_ID)
L_LEAD_LEG = LSS(L_LEAD_LEG_ID)
R_HIND_LEG = LSS(R_HIND_LEG_ID)
L_HIND_LEG = LSS(L_HIND_LEG_ID)

# Common LSS class for broadcasting to all servos
ALL = LSS(BROADCAST_ID)

# array of servos, so they can be individually addressed in a `for` loop
lss_array = [
    R_LEAD_LEG,
    L_LEAD_LEG,
    L_HIND_LEG,
    R_HIND_LEG,
]

# Represents the adjustment made to each leg's virtul angular position,
# so that all legs are aligned in real space.
# Calibrated for each individual robot.
# Calibration offsets for Elijah's Robot
cal = [
    0,
    0,
    0,
    0
]



