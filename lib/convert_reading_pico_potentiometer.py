from convert_minMax_actual_to_desired import convert_minMax_actual_to_desired
from constants import PICO

def convert_reading_pico_potentiometer(outputValue):    
    minOutputActual = 224
    maxOutputActual = 65535
    minOutputDesired = 0
    maxOutputDesired = PICO["VOLTAGE"]
    
    return convert_minMax_actual_to_desired(minOutputActual, maxOutputActual, minOutputDesired, maxOutputDesired, outputValue)