from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired
from _constants import (
    PICO_MAX_PWM as MAX_PWM,
    PICO_MIN_PWM_ACTUAL as MIN_PWM,
    PICO_MIN_VOLTAGE as MIN_VOLTAGE,
    PICO_MAX_VOLTAGE as MAX_VOLTAGE,
)


def convert_output_pico_potentiometer(value, minOutputDesired=None, maxOutputDesired=None):
    minOutputActual = MIN_PWM
    maxOutputActual = MAX_PWM
    minOutputDesired = minOutputDesired or MIN_VOLTAGE
    maxOutputDesired = maxOutputDesired or MAX_VOLTAGE

    return convert_minMax_actual_to_desired(
        minOutputActual,
        maxOutputActual,
        minOutputDesired,
        maxOutputDesired,
        value,
    )
