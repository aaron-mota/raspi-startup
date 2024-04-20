from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired
from _constants import (
    PICO_MAX_PWM as MAX_PWM,
    PICO_MIN_PWM as MIN_PWM,
    PICO_MIN_VOLTAGE as MIN_VOLTAGE,
    PICO_MAX_VOLTAGE as MAX_VOLTAGE,
)


def convert_output_voltage_to_pwm(value, minOutputDesired=MIN_PWM, maxOutputDesired=MAX_PWM):
    minOutputActual = MIN_VOLTAGE
    maxOutputActual = MAX_VOLTAGE

    print(minOutputActual, maxOutputActual, minOutputDesired, maxOutputDesired, value)

    result = convert_minMax_actual_to_desired(
        minOutputActual,
        maxOutputActual,
        minOutputDesired,
        maxOutputDesired,
        value,
    )

    return int(result)
