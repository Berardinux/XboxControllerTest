import math
SHOULDER_LENGTH = 200
ELBOW_LENGTH = 200

def moveToPos(x, y):
    h1 = math.sqrt(x**2 + y**2)

    if  h1 > (SHOULDER_LENGTH + ELBOW_LENGTH):
            print("Error: Target is out of reach")
            return None, None
    

    θ1 = round(math.degrees(math.asin(y/h1)))

    θ2 = math.degrees(math.acos((h1/2)/SHOULDER_LENGTH))

    an1 = θ1 + θ2

    #θ3 = 90 - θ2
    θ3 = math.degrees(math.acos((SHOULDER_LENGTH**2 + ELBOW_LENGTH**2 - h1**2) / (2 * SHOULDER_LENGTH * ELBOW_LENGTH)))
    #θ4 = θ3*2
    θ4 = 180 - θ3

    θ5 = 180 - θ4

    an2 = -1 * (90 - θ5)

    return an1, an2

#moveToPos(250, 250)
