from machine import Pin, PWM, ADC
from time import sleep
from _pins import PIN_GP15__20 as PIN_PWM, PIN_ADC0__31_10b as PIN_ADC0
from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm

# from _convert_percentage_to_voltage import convert_percentage_to_voltage
from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage

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

# EXAMPLE THREE: Setting value via potentiometer
while True:
    try:
        valueRaw = potentiometer.read_u16()
        desiredVoltage = convert_output_pwm_to_voltage(valueRaw)
        pwmValue = convert_output_voltage_to_pwm(desiredVoltage)
        analogOut.duty_u16(pwmValue)
        sleep(0.5)
        print("Raw: ", potentiometer.read_u16(), "Converted V: ", desiredVoltage, "Converted PWM: ", pwmValue)
    except KeyboardInterrupt:
        break
