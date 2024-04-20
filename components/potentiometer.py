import machine
from utime import sleep
from _convert_output_pwm_to_voltage import convert_output_pwm_to_voltage
from _pins import PIN_ADC0__31_10b as PIN_ADC0


potentiometer = machine.ADC(PIN_ADC0)

while True:
    try:
        valueRaw = potentiometer.read_u16()
        valueConverted = convert_output_pwm_to_voltage(valueRaw, 0, 3.3)
        print("Raw: ", valueRaw, "Converted: ", valueConverted, "V")
        sleep(0.5)
    except KeyboardInterrupt:
        break
print("Finished.")
