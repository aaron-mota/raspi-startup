from imu import MPU6050
from machine import I2C, Pin
import math
import time

from _trigonometry import convertRadiansToDegrees


i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
mpu = MPU6050(i2c)

rollG = 0
pitchG = 0

rollComp = 0
pitchComp = 0

errorR = 0
errorP = 0

yaw = 0
tLoop = 0
cnt = 0

COMPLIMENTARY_FILTER = 0.995
UNFILTERED = 0.005
EFFECTIVE_ZERO_TILT = 0.2

while True:
    tStart = time.ticks_ms()

    # ACCELEROMETER
    xAccel = mpu.accel.x
    yAccel = mpu.accel.y
    zAccel = mpu.accel.z

    rollA = -convertRadiansToDegrees(math.atan(xAccel / zAccel), 2)
    pitchA = convertRadiansToDegrees(math.atan(yAccel / zAccel), 2)

    # GYROSCOPE
    xGyro = mpu.gyro.x
    yGyro = mpu.gyro.y
    zGyro = mpu.gyro.z

    rollG = rollG + yGyro * tLoop
    pitchG = pitchG + xGyro * tLoop

    # COMPLIMENTARY FILTER
    rollCompRaw = (rollA * UNFILTERED) + (COMPLIMENTARY_FILTER * (rollComp + yGyro * tLoop) + errorR * UNFILTERED)
    pitchCompRaw = (pitchA * UNFILTERED) + (COMPLIMENTARY_FILTER * (pitchComp + xGyro * tLoop) + errorP * UNFILTERED)
    rollComp = rollCompRaw if abs(rollCompRaw) > EFFECTIVE_ZERO_TILT else 0
    pitchComp = pitchCompRaw if abs(pitchCompRaw) > EFFECTIVE_ZERO_TILT else 0

    # ERROR
    errorRRaw = errorR + (rollA - rollComp) * tLoop
    errorPRaw = errorP + (pitchA - pitchComp) * tLoop
    errorR = errorRRaw if rollComp != 0 else 0
    errorP = errorPRaw if pitchComp != 0 else 0

    # PRINTING
    cnt = cnt + 1
    if cnt == 10:
        cnt = 0
        print("RA: ", rollA, "PA: ", pitchA, "RC: ", rollComp, "PC: ", pitchComp)
        # print('RA: ',rollA,'RC: ',rollComp)

    # FINISH LOOP
    tStop = time.ticks_ms()
    tLoop = (tStop - tStart) * 0.001
