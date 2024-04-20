from _constants import (
    PICO_MIN_VOLTAGE as MIN_VOLTAGE,
    PICO_MAX_VOLTAGE as MAX_VOLTAGE,
)


# e.g. percentage = 0.5
def convert_percentage_to_voltage(percentage):
    return (MAX_VOLTAGE - MIN_VOLTAGE) * percentage + MIN_VOLTAGE
