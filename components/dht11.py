from machine import Pin, PWM, ADC, I2C
import utime as time

# from dht import DHT11, InvalidPulseCount
from dht_updated import DHT11, InvalidPulseCount

from _pins import (
    PIN_GP16__21_20b__SPI0_RX__I2C0_SDA__UART1_TX as PIN_GP16,
    # PIN_GP17__22_19b__SPI0_CSn__I2C0_SCL__UART1_RX as PIN_GP17,
)

from _temperature import (
    convert_celsius_to_fahrenheit,
)

# from _constants import PICO_MIN_PWM_ACTUAL, PICO_MAX_PWM

# from _convert_output_voltage_to_pwm import convert_output_voltage_to_pwm
# from _convert_percentage_to_voltage import convert_percentage_to_voltage
# from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
# from _convert_minMax_actual_to_desired import convert_minMax_actual_to_desired

#################
# NOTES
#################
# DHT11 (Temperature and Humidity Sensor)
# - fritzing (https://github.com/adafruit/Fritzing-Library/tree/master/parts) (https://forum.fritzing.org/t/humidity-and-temperature-sensor-dht11/6307/7)
# - kepler kit (https://docs.sunfounder.com/projects/kepler-kit/en/latest/pyproject/py_dht11.html)
# -


#################
# HELPERS
#################


#################
# SETUP
#################
pin_data = Pin(PIN_GP16, Pin.IN, Pin.PULL_UP)
sensor = DHT11(pin_data)

#################
# PROGRAM
#################

## CONFIG
time.sleep(5)  # initial delay


try:
    while True:
        try:
            #################
            # (0) CONFIG
            #################

            #################
            # (1) GET INPUT
            #################
            sensor.measure()
            tempF = convert_celsius_to_fahrenheit(sensor.temperature)
            humidity = sensor.humidity
            string = f"Temperature: {tempF}°F\nHumidity: {humidity}%\n"
            print(string)
            time.sleep(4)

            #################
            # (2) SET OUTPUT
            #################

            #################
            # (final) CONFIG
            #################

            time.sleep(0.02)
        except InvalidPulseCount as e:
            print("Bad pulse count - retrying ...")
except KeyboardInterrupt:
    print("Bye!")
