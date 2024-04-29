from machine import Pin, PWM, ADC, I2C
import time
from imu import MPU6050
import math

from _pins import (
    PIN_GP16__21_20b__SPI0_RX__I2C0_SDA__UART1_TX as PIN_GP16,
    PIN_GP17__22_19b__SPI0_CSn__I2C0_SCL__UART1_RX as PIN_GP17,
)

from _trigonometry import (
    getTiltDegreesFromAcceleration,
    getTiltDegreesFromAccelerationPitchRoll,
)

# from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM

# from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm
# from _convert_percentage_to_voltage import convert_percentage_to_voltage
# from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
# from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

#################
# NOTES
#################
# MPU6050
# - https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/components_basic/05-component_mpu6050.html
# - components: 3-axis gyroscope, 3-axis accelerometer
# - z-axis = 1G (acceleration due to gravity)


#################
# HELPERS
#################


#################
# SETUP
#################
i2c = I2C(0, sda=Pin(PIN_GP16), scl=Pin(PIN_GP17), freq=400000)
# why freq=400000? - https://docs.micropython.org/en/latest/library/machine.I2C.html
# - "The frequency parameter is an optional integer giving the I2C clock frequency in Hz. The default is 400kHz."
# - "The frequency is a maximum value. The actual frequency may be less, depending on the hardware capabilities."
# - SDA and SCL are the data and clock lines, respectively.
# - "The I2C bus is a two-wire half-duplex serial bus with a single clock line and a single data line."

mpu = MPU6050(i2c)

#################
# PROGRAM
#################

## CONFIG (GYROSCOPE)
tLoop = 0  # seconds
roll = 0
pitch = 0
yaw = 0
count = 0


try:
    while True:
        #################
        # (0) CONFIG
        #################
        tStart = time.ticks_ms()

        #################
        # (1) GET INPUT
        #################
        # MPU

        # ACCELERATION
        ###################
        # xAccel, yAccel, zAccel = mpu.accel.xyz
        # print(f"(Acceleration) x: {xAccel} G, y: {yAccel} G, z: {zAccel} G         ", end="\r")

        # TILT (PITCH, ROLL) (from acceleration) (normal/perpendicular vector to gravity)
        # https://youtu.be/GWYy121rAOE?si=eB_4Iv7L3K199ZA_&t=666

        # (1) General Tilt
        # tilt = getTiltDegreesFromAcceleration(float(zAccel))  # pitch or roll
        # print(f"(Tilt) Pitch: {tilt} deg      ", end="\r")

        # (2) Pitch & Roll
        # can use a "low pass filter" to smooth out the values (noise vs real signals; trade-off = responsiveness)
        # - e.g. confidenceSensor, confidenceHistoricalData (https://youtu.be/3YqGIg4crEk?si=EaJhBTlsz5ivz3NY)
        # tiltPitch = getTiltDegreesFromAccelerationPitchRoll(yAccel, zAccel, 2)  # pitch or roll
        # tiltRoll = getTiltDegreesFromAccelerationPitchRoll(xAccel, zAccel, 2)  # pitch or roll
        # print(f"(Tilt) Pitch: {tiltPitch} deg, Roll: {tiltRoll} deg      ", end="\r")

        # GYROSCOPE
        ###################
        # - ...acceleration = isn't great for rotation (e.g. errors d/t vibration, horizontal acceleration, etc.)
        # - angular velocity & angle (https://youtu.be/XZIJasvCB44?si=cOIpMg6zKyIsLh_1&t=473)
        # -...gyroscope = "drift" problem

        xGyro, yGyro, zGyro = mpu.gyro.xyz
        # roll = roll + xGyro * tLoop
        # pitch = pitch + yGyro * tLoop
        roll = roll + yGyro * tLoop
        pitch = pitch + xGyro * tLoop
        yaw = yaw + zGyro * tLoop
        # print(f"(Gyroscope) x: {xGyro} deg/s, y: {yGyro} deg/s, z: {zGyro} deg/s       ", end="\r")

        #################
        # (2) SET OUTPUT
        #################

        #################
        # (final) CONFIG
        #################
        count += 1
        if count % 50 == 0:
            print(f"Pitch: {pitch} deg, Roll: {roll} deg, Yaw: {yaw} deg/s")

        tEnd = time.ticks_ms()
        tLoop = time.ticks_diff(tEnd, tStart) / 1000

        time.sleep(0.02)
except KeyboardInterrupt:
    print("Bye!")


# MPU6050
# https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/components_basic/05-component_mpu6050.html
# - components: 3-axis gyroscope, 3-axis accelerometer
