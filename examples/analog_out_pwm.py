from machine import Pin, PWM
from time import sleep
from _pins import PIN_GP15__20 as PIN_PWM
from _convert_output_pico_potentiometer import convert_output_pico_potentiometer

# from _convert_percentage_to_voltage import convert_percentage_to_voltage

# Define the PWM pin
analogOut = PWM(Pin(PIN_PWM))
analogOut.freq(1000)  # (1000 Hz) (default is 500 Hz) (one period = 1 / frequency = 1 / 1000 = 0.001 s = 1 ms)
analogOut.duty_u16(0)  # (0-65535) (0 = 0 V) (65535 = 3.3 V)


# EXAMPLE ONE: Setting voltage
while True:
    desiredVoltage = float(input("Enter a voltage (0-3.3 V): "))
    if desiredVoltage < 0 or desiredVoltage > 3.3:
        print("Invalid voltage. Please enter a voltage between 0 and 3.3 V.")
        continue
    pwmValue = convert_output_pico_potentiometer(desiredVoltage)
    analogOut.duty_u16(pwmValue)
    sleep(0.1)
    print("Raw: ", desiredVoltage, "Converted: ", pwmValue)

# EXAMPLE TWO: Setting percentage (given numerical value between 0 and 1)
# while True:
#     desiredPercentage = float(input("Enter a percentage (0-1): "))
#     if desiredPercentage < 0 or desiredPercentage > 1:
#         print("Invalid percentage. Please enter a percentage between 0 and 1.")
#         continue
#     desiredVoltage = convert_percentage_to_voltage(desiredPercentage)
#     pwmValue = convert_output_pico_potentiometer(desiredVoltage)
#     analogOut.duty_u16(pwmValue)
#     sleep(0.1)
