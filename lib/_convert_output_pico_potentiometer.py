from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired
from _constants import PICO


def convert_output_pico_potentiometer(value, minOutputDesired, maxOutputDesired):
    minOutputActual = 224
    maxOutputActual = 65535
    # minOutputDesired = 0
    # maxOutputDesired = PICO["VOLTAGE"]

    return convert_minMax_actual_to_desired(
        minOutputActual,
        maxOutputActual,
        minOutputDesired,
        maxOutputDesired,
        value,
    )
