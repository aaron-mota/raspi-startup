# from machine import Pin
import machine
from utime import sleep
from convert_reading_pico_potentiometer import convert_reading_pico_potentiometer 

#############  
# number values = GPIO number
############# 
# ADC = Analog to Digital Converter
pinADC0_26 = 26
pinADC1_27 = 27
pinADC2_28 = 28

potentiometer = machine.ADC(pinADC0_26)
# ACTUAL (OUTPUT)
# min: 224 (or less)
# max: 65535
# CONVERSION NEEDED
# min: 0 (V)
# max: 3.3 (V)


while True:
    try:
        valueRaw = potentiometer.read_u16()
        valueConverted = convert_reading_pico_potentiometer(valueRaw)
        print("Raw: ", valueRaw, "Converted: ", valueConverted, "V")
        sleep(0.5)
    except KeyboardInterrupt:
        break
print("Finished.")

