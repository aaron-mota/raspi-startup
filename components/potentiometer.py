import machine
from utime import sleep
from _convert_reading_pico_potentiometer import convert_reading_pico_potentiometer
from _constants import PIN_ADC0__31_10b as PIN_ADC0


potentiometer = machine.ADC(PIN_ADC0)

while True:
    try:
        valueRaw = potentiometer.read_u16()
        valueConverted = convert_reading_pico_potentiometer(valueRaw)
        print("Raw: ", valueRaw, "Converted: ", valueConverted, "V")
        sleep(0.5)
    except KeyboardInterrupt:
        break
print("Finished.")
