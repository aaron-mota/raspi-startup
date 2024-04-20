from machine import Pin, PWM, ADC
from time import sleep
from _pins import (
    PIN_ADC0__31_10b as PIN_ADC0,
    PIN_GP7__10 as PIN_LED_BLUE,
    PIN_GP8__11 as PIN_LED_GREEN,
    PIN_GP9__12 as PIN_LED_RED,
)
from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM
from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm

# from _convert_percentage_to_voltage import convert_percentage_to_voltage
from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

# Step 1: Define the pins
potentiometer = ADC(PIN_ADC0)
ledRed = PWM(Pin(PIN_LED_RED))
ledGreen = PWM(Pin(PIN_LED_GREEN))
ledBlue = PWM(Pin(PIN_LED_BLUE))

# Step 2: Define the PWM frequency & duty cycle
ledRed.freq(1000)
ledRed.duty_u16(0)
ledGreen.freq(1000)
ledGreen.duty_u16(0)
ledBlue.freq(1000)
ledRed.duty_u16(0)

# Step 3: Define the RGB values

# # EXAMPLE 1: Program-defined RGB values
# while True:
#     ledRed.duty_u16(PICO_MAX_PWM)
#     ledGreen.duty_u16(0)
#     ledBlue.duty_u16(0)
#     sleep(0.1)


# EXAMPLE 2: Potentiometer-driven input
while True:
    MAX_DESIRED_VALUE = 100

    try:
        valueRaw = potentiometer.read_u16()
        scaledValue = round(
            convert_minMax_actual_to_desired(PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM, 0, MAX_DESIRED_VALUE, valueRaw)
        )

        # 0 to 100 (scale up/down R/G/B values in between)
        scaledValueRed = 0
        scaledValueGreen = 0
        scaledValueBlue = 0

        if scaledValue <= 50:
            scaledValueRed = 100 - convert_minMax_actual_to_desired(0, 50, 0, 100, scaledValue)
            scaledValueGreen = convert_minMax_actual_to_desired(0, 50, 0, 100, scaledValue)
            scaledValueBlue = 0
        else:
            scaledValueRed = 0
            scaledValueGreen = 100 - convert_minMax_actual_to_desired(50, 100, 0, 100, scaledValue)
            scaledValueBlue = convert_minMax_actual_to_desired(50, 100, 0, 100, scaledValue)

        # convert 0-100 to 0-65535
        pwmValueRed = round(convert_minMax_actual_to_desired(0, MAX_DESIRED_VALUE, 0, PICO_MAX_PWM, scaledValueRed))
        pwmValueGreen = round(convert_minMax_actual_to_desired(0, MAX_DESIRED_VALUE, 0, PICO_MAX_PWM, scaledValueGreen))
        pwmValueBlue = round(convert_minMax_actual_to_desired(0, MAX_DESIRED_VALUE, 0, PICO_MAX_PWM, scaledValueBlue))

        ledRed.duty_u16(pwmValueRed)
        ledGreen.duty_u16(pwmValueGreen)
        ledBlue.duty_u16(pwmValueBlue)

        sleep(0.2)

        print(
            "Scaled: ",
            scaledValue,
            f"{round(scaledValueRed)}/{round(scaledValueGreen)}/{round(scaledValueBlue)}",
            f"{round(pwmValueRed)}/{round(pwmValueGreen)}/{round(pwmValueBlue)}",
        )

    except KeyboardInterrupt:
        ledRed.duty_u16(0)
        ledGreen.duty_u16(0)
        ledBlue.duty_u16(0)
        break
