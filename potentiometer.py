# from machine import Pin
import machine
from utime import sleep

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

def convert_potentiometer_output_to_voltage(val):
    # when OUTPUT is 224, should be 0 after conversion
    # when OUTPUT is 65535, should be 3.3 after conversion
    # when value is between, should be between 0 and 3.3
    
    # slope of line (m): (y2 - y1) / (x2 - x1)
    minOutputActual = 224 # x1
    maxOutputActual = 65535 # x2
    minOutputDesired = 0 # y1
    maxOutputDesired = 3.3 # y2
    
    y2 = maxOutputDesired
    y1 = minOutputDesired
    x2 = maxOutputActual
    x1 = minOutputActual
    
    m = (y2 - y1) / (x2 - x1)
    # y - y1 = m(x - x1)
    y = m * (val) - m * x1 + y1
    
    # handle inaccurate "lowest possible" output value
    if y < 0:
        y = 0
        
    # handle inaccurate "highest possible" output value
    if y > 3.3:
        y = 3.3
        
    return y




while True:
    try:
        valueRaw = potentiometer.read_u16()
        valueConverted = convert_potentiometer_output_to_voltage(valueRaw)
        print("Raw: ", valueRaw, "Converted: ", valueConverted, "V")
        sleep(0.5)
    except KeyboardInterrupt:
        break
print("Finished.")

