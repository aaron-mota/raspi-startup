from machine import Pin, PWM, ADC
from time import sleep

from _pins import (
    PIN_GP15__20 as PIN_GP15,
    PIN_GP26__31_10b as PIN_GP26,
)

from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM

# from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm
# from _convert_percentage_to_voltage import convert_percentage_to_voltage
# from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
# from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

#################
# NOTES
#################
# - 0.5ms to 2.5ms pulse width (duty cycle)
#   - 0 degrees: 0.5ms pulse
#   - 90 degrees: 1.5ms pulse
#   - 180 degrees: 2.5ms pulse
# - 20ms period // 50Hz frequency (freq = 1 / period) (1 / 0.02 = 50 Hz)
#
# PWM
# - freq: 50Hz
# - duty_u16: 0 to 65535
# - writeValue = int(round(65535 * (pulseWidth / 20)))


#################
# HELPERS
#################
PERIOD = 20

MIN_PULSE_WIDTH = 0.5
MAX_PULSE_WIDTH = 2.5
MAX_DEGREES = 180


def convertPulseWidthToPWMValue(pulseWidth: float) -> int:
    return int(round(PICO_MAX_PWM * (pulseWidth / PERIOD)))


def convertDegreesToPulseWidth(degrees: int) -> float:
    # 0.5ms to 2.5ms pulse width (duty cycle)
    # 0 degrees: 0.5ms pulse
    # 90 degrees: 1.5ms pulse
    # 180 degrees: 2.5ms pulse
    return MIN_PULSE_WIDTH + ((MAX_PULSE_WIDTH - MIN_PULSE_WIDTH) / MAX_DEGREES) * degrees


#################
# SETUP
#################
# Step 1: Define the pins
servo = PWM(Pin(PIN_GP15))
servo.freq(50)  # 50Hz

potentiometer = ADC(Pin(PIN_GP26))

#################
# PROGRAM
#################

degrees = 0
try:
    while True:
        #################
        # (1) GET DEGREES
        #################
        # HARD-CODED
        # degrees = 180

        # HARD-CODED (AUTO TOGGLE)
        # degrees = 90 if degrees == 0 else 180 if degrees == 90 else 0 # auto toggle between 0, 90, 180

        # USER INPUT
        # result = int(input("Enter degrees (0 to 180): "))
        # degrees = result

        # POTENTIOMETER
        pwmValueInput = potentiometer.read_u16()
        degrees = int(round((MAX_DEGREES / PICO_MAX_PWM) * pwmValueInput))  # not sure if this is correct (didn't test it)

        #################
        # (2) SET SERVO
        #################
        pulseWidth = convertDegreesToPulseWidth(degrees)
        pwmValue = convertPulseWidthToPWMValue(pulseWidth)
        servo.duty_u16(pwmValue)
        sleep(0.02)
        # print(f"degrees: {degrees}, pulseWidth: {pulseWidth}, pwmValue: {pwmValue}")
except KeyboardInterrupt:
    servo.duty_u16(0)
