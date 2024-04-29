import math

####################
# TRIGONOMETRY
####################

# CIRCLE
##############
# (main)
# radians = degrees / 360 * 2 * pi
# degrees = radians / (2 * pi) * 360
# theta = degrees or radians
# x = r * cos(radians) # computer programs are generally in radians
# y = r * sin(radians) # computer programs are generally in radians
# (additional)
# r = sqrt(x^2 + y^2)
# theta = atan(y / x)

ACCELERATION_DUE_TO_GRAVITY_G = 1.0


def convertDegreesToRadians(degrees: float) -> float:
    return degrees / 360 * (2 * math.pi)


def convertRadiansToDegrees(radians: float) -> float:
    return radians / (2 * math.pi) * 360


def getXYFromThetaDegrees(degrees: float, r=1) -> tuple:
    radians = convertDegreesToRadians(degrees)
    x = r * math.cos(radians)
    y = r * math.sin(radians)
    return x, y


def getXYFromThetaRadians(radians: float, r=1) -> tuple:
    x = r * math.cos(radians)
    y = r * math.sin(radians)
    return x, y


def getRadiusFromXY(x: float, y: float) -> float:
    return math.atan(y / x)


# def getRadiusFromXY(x: float, y: float) -> float:
#     return math.sqrt(x**2 + y**2)


def getThetaRadiansFromXY(x: float, y: float) -> float:
    return math.atan(y / x)


def getThetaRadiansFromX(x: float) -> float:
    return math.acos(x)


def getThetaRadiansFromY(y: float) -> float:
    return math.asin(y)


def getThetaDegreesFromXY(x: float, y: float) -> float:
    radians = math.atan(y / x)
    return convertRadiansToDegrees(radians)


def getThetaDegreesFromX(x: float) -> float:
    radians = math.acos(x)
    return convertRadiansToDegrees(radians)


def getThetaDegreesFromY(y: float) -> float:
    radians = math.asin(y)
    return convertRadiansToDegrees(radians)


def getThetaDegreesFromAcceleration(reading: float, constant=ACCELERATION_DUE_TO_GRAVITY_G) -> float:
    radians = 0.0

    reading = max(min(1.0, reading), -1.0)
    multiplier = 1 if reading >= 0 else -1

    if constant == 0:
        radians = math.atan(reading)
    else:
        adjacentOverHypotenuse = reading / constant
        radians = math.acos(adjacentOverHypotenuse)
    return convertRadiansToDegrees(radians) * multiplier


def getTiltDegreesFromAcceleration(reading: float, constant=ACCELERATION_DUE_TO_GRAVITY_G) -> float:
    return getThetaDegreesFromAcceleration(reading, constant)
