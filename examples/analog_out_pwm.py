from machine import Pin, PWM, ADC
from time import sleep
from _pins import PIN_GP15__20 as PIN_PWM, PIN_ADC0__31_10b as PIN_ADC0
from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM
from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm

# from _convert_percentage_to_voltage import convert_percentage_to_voltage
from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

potentiometer = ADC(PIN_ADC0)

# Define the PWM pin
analogOut = PWM(Pin(PIN_PWM))
analogOut.freq(1000)  # (1000 Hz) (default is 500 Hz) (one period = 1 / frequency = 1 / 1000 = 0.001 s = 1 ms)
analogOut.duty_u16(0)  # (0-65535) (0 = 0 V) (65535 = 3.3 V)


# EXAMPLE ONE: Setting voltage
# while True:
#     desiredVoltage = float(input("Enter a voltage (0-3.3 V): "))
#     if desiredVoltage < 0 or desiredVoltage > 3.3:
#         print("Invalid voltage. Please enter a voltage between 0 and 3.3 V.")
#         continue
#     pwmValue = convert_output_voltage_to_pwm(desiredVoltage)
#     analogOut.duty_u16(pwmValue)
#     sleep(0.1)
#     print("Raw: ", desiredVoltage, "Converted: ", pwmValue)

# EXAMPLE TWO: Setting percentage (given numerical value between 0 and 1)
# while True:
#     desiredPercentage = float(input("Enter a percentage (0-1): "))
#     if desiredPercentage < 0 or desiredPercentage > 1:
#         print("Invalid percentage. Please enter a percentage between 0 and 1.")
#         continue
#     desiredVoltage = convert_percentage_to_voltage(desiredPercentage)
#     pwmValue = convert_output_voltage_to_pwm(desiredVoltage)
#     analogOut.duty_u16(pwmValue)
#     sleep(0.1)
#     print("Raw: ", desiredPercentage, "Converted V: ", desiredVoltage, "Converted PWM: ", pwmValue)

# EXAMPLE THREE: Setting voltage/pwm via potentiometer-driven input (dimmable LED)
# while True:
#     try:
#         valueRaw = potentiometer.read_u16()
#         # 1: difficult way (convert raw value to voltage, then convert voltage to pwm)
#         desiredVoltage = convert_output_pwm_to_voltage(valueRaw)
#         pwmValue = convert_output_voltage_to_pwm(desiredVoltage)
#         analogOut.duty_u16(pwmValue)
#         print("Raw: ", potentiometer.read_u16(), "Converted V: ", desiredVoltage, "Converted PWM: ", pwmValue)
#         # # 2: easy way (convert raw value to pwm directly)
#         # # NOTE: HOWEVER, this method is not as accurate as the first method (e.g. lowest input from potentiometer is not 0, it's ~224)
#         # analogOut.duty_u16(valueRaw)
#         # print("Raw: ", potentiometer.read_u16())

#         sleep(0.5)
#     except KeyboardInterrupt:
#         break

# # EXAMPLE FOUR: Potentiometer-driven input, but using 16 "steps" (2^0 - 2^16)
# while True:
#     try:
#         valueRaw = potentiometer.read_u16()
#         scaledValue = convert_minMax_actual_to_desired(PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM, 0, 16, valueRaw)
#         # y = 2^x (using 16 "steps" from 0 to 16, where 0 = 2^0 and 16 = 2^16)
#         x = round(scaledValue)
#         pwmValue = 2**x if x > 0 else 0  # 2^0 = 1... want to be able to turn off LED
#         analogOut.duty_u16(pwmValue)
#         # sleep(0.1)
#         print("Raw: ", potentiometer.read_u16(), "x: ", x, "Converted PWM: ", pwmValue)
#     except KeyboardInterrupt:
#         break

# # EXAMPLE 5: Potentiometer-driven input, but using X "steps" (linear)
# # NOTE: not visibly noticable difference in brightness between each step (e.g. at higher values, can't see the LED adjusting with smaller changes in potentiometer)
# while True:
#     CONSTANT = (PICO_MAX_PWM - PICO_MIN_PWM_ACTUAL) / 50
#     STEPS = 50

#     try:
#         valueRaw = potentiometer.read_u16()
#         scaledValue = convert_minMax_actual_to_desired(PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM, 0, STEPS, valueRaw)
#         # y = CONSTANT*x
#         x = round(scaledValue)
#         pwmValue = round(CONSTANT * x)
#         analogOut.duty_u16(pwmValue)
#         # sleep(0.1)
#         print("Raw: ", potentiometer.read_u16(), "C: ", CONSTANT, "x: ", x, "Converted PWM: ", pwmValue)
#     except KeyboardInterrupt:
#         analogOut.duty_u16(0)
#         break

# EXAMPLE 6: Potentiometer-driven input, but using X "steps" (exponential)
# NOTE: visibly noticable difference in brightness between each step (e.g. at higher values, can see the LED adjusting with smaller changes in potentiometer)
while True:
    STEPS = 50
    CONSTANT = (PICO_MAX_PWM - PICO_MIN_PWM_ACTUAL) ** (1 / STEPS)

    try:
        valueRaw = potentiometer.read_u16()
        scaledValue = convert_minMax_actual_to_desired(PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM, 0, STEPS, valueRaw)
        # y = CONSTANT**x
        x = round(scaledValue)
        pwmValue = round(CONSTANT**x)
        analogOut.duty_u16(pwmValue)
        # sleep(0.1)
        print("Raw: ", potentiometer.read_u16(), "C: ", CONSTANT, "x: ", x, "Converted PWM: ", pwmValue)
    except KeyboardInterrupt:
        analogOut.duty_u16(0)
        break
