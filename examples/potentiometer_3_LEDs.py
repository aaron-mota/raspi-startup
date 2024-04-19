import machine
from utime import sleep
from _convert_output_pico_potentiometer import convert_output_pico_potentiometer
from _pins import (
    PIN_ADC0__31_10b as PIN_ADC0,
    PIN_GP15__20 as PIN_LED_GREEN,
    PIN_GP12__16 as PIN_LED_YELLOW,
    PIN_GP10__14 as PIN_LED_RED,
)


potentiometer = machine.ADC(PIN_ADC0)
led_green = machine.Pin(PIN_LED_GREEN, machine.Pin.OUT)
led_yellow = machine.Pin(PIN_LED_YELLOW, machine.Pin.OUT)
led_red = machine.Pin(PIN_LED_RED, machine.Pin.OUT)

while True:
    try:
        valueRaw = potentiometer.read_u16()
        valueConverted = convert_output_pico_potentiometer(valueRaw, 0, 100)
        print("Raw: ", valueRaw, "Converted: ", valueConverted, "V")
        sleep(0.5)

        if valueConverted < 33:
            led_red.value(1)
            led_yellow.value(0)
            led_green.value(0)
        elif valueConverted < 66:
            led_red.value(0)
            led_yellow.value(1)
            led_green.value(0)
        else:
            led_red.value(0)
            led_yellow.value(0)
            led_green.value(1)

    except KeyboardInterrupt:
        break
led_red.value(0)
led_yellow.value(0)
led_green.value(0)
print("Finished.")
