# from machine import Pin
import machine
from utime import sleep
from _convert_reading_pico_potentiometer import convert_reading_pico_potentiometer 

#############  
# number values = GPIO number
############# 
# ADC = Analog to Digital Converter
pin26_ADC0 = 26
pin27_ADC1 = 27
pin28_ADC2 = 28

potentiometer = machine.ADC(pin26_ADC0)
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

