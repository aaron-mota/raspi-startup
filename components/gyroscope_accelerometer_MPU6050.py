from machine import Pin, PWM, ADC, I2C
from time import sleep
from imu import MPU6050
import math

from _pins import (
    PIN_GP16__21_20b__SPI0_RX__I2C0_SDA__UART1_TX as PIN_GP16,
    PIN_GP17__22_19b__SPI0_CSn__I2C0_SCL__UART1_RX as PIN_GP17,
)

from _trigonometry import (
    getTiltDegreesFromAcceleration,
    getTiltDegreesFromAccelerationPitch,
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

try:
    while True:
        #################
        # (1) GET INPUT
        #################
        # MPU

        # ACCELERATION
        xAccel, yAccel, zAccel = mpu.accel.xyz
        # print(f"(Acceleration) x: {xAccel} G, y: {yAccel} G, z: {zAccel} G         ", end="\r")

        # TILT (PITCH, ROLL) (from acceleration) (normal/perpendicular vector to gravity)
        # https://youtu.be/GWYy121rAOE?si=eB_4Iv7L3K199ZA_&t=666
        # General Tilt
        # tilt = getTiltDegreesFromAcceleration(float(zAccel))  # pitch or roll
        # print(f"(Tilt) Pitch: {tilt} deg      ", end="\r")

        # Pitch & Roll
        tiltPitch = getTiltDegreesFromAccelerationPitch(yAccel, zAccel, 2)  # pitch or roll
        # print(f"(Tilt) Pitch: {tiltPitch} deg      ")
        # print(f"(Tilt) Pitch: {tiltPitch} deg      ", end="\r")
        tiltRoll = getTiltDegreesFromAccelerationPitch(xAccel, zAccel, 2)  # pitch or roll
        print(f"(Tilt) Pitch: {tiltPitch} deg, Roll: {tiltRoll} deg      ", end="\r")

        # GYROSCOPE
        # xGyro, yGyro, zGyro = mpu.gyro.xyz
        # print(f"(Gyroscope) x: {xGyro} deg/s, y: {yGyro} deg/s, z: {zGyro} deg/s       ", end="\r")

        #################
        # (2) SET OUTPUT
        #################

        sleep(0.1)
except KeyboardInterrupt:
    print("Bye!")


# MPU6050
# https://docs.sunfounder.com/projects/ultimate-sensor-kit/en/latest/components_basic/05-component_mpu6050.html
# - components: 3-axis gyroscope, 3-axis accelerometer
