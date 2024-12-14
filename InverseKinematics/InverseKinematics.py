import math
import numpy as np

SHOULDER_LENGTH = 200
ELBOW_LENGTH = 200

def moveToPos(x, y):
    h1 = math.sqrt(x**2 + y**2)

    if h1 == 0:
        return None, None, None, None

    if h1 > (SHOULDER_LENGTH + ELBOW_LENGTH):
        return None, None, None, None
    
    θ1 = round(math.degrees(math.asin(y/h1)))
    θ2 = math.degrees(math.acos((h1/2)/SHOULDER_LENGTH))
    an1 = θ1 + θ2
    θ3 = math.degrees(math.asin((h1/2)/SHOULDER_LENGTH)
    #θ3 = 90 - θ2
    θ4 = θ3 * 2
    θ5 = 180 - θ4
    an2 = (90 - θ5)

    if 0 <= an1 <= 180:
        spw = np.interp(an1, [0, 180], [1600, 440])
    else:
        spw = None

    if 0 <= an2 <= 180:
        epw = np.interp(an2, [0, 180], [1880, 720])
    else:
        epw = None

    return an1, an2, spw, epw
