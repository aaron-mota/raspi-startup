from machine import Pin, PWM, ADC, I2C
import utime as time
from imu import MPU6050
import math

# from _pins import (
#     # PIN_GP16__21_20b__SPI0_RX__I2C0_SDA__UART1_TX as PIN_GP16,
#     # PIN_GP17__22_19b__SPI0_CSn__I2C0_SCL__UART1_RX as PIN_GP17,
# )

# from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM

# from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm
# from _convert_percentage_to_voltage import convert_percentage_to_voltage
# from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
# from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

#################
# NOTES
#################
# NAME_OF_COMPONENT
# - [link]
# - components: [inner components]
# -


#################
# HELPERS
#################


#################
# SETUP
#################


#################
# PROGRAM
#################

## CONFIG


try:
    while True:
        #################
        # (0) CONFIG
        #################

        #################
        # (1) GET INPUT
        #################

        #################
        # (2) SET OUTPUT
        #################

        #################
        # (final) CONFIG
        #################

        time.sleep(0.02)
except KeyboardInterrupt:
    print("Bye!")
