from machine import Pin
from _convert_output_pico_potentiometer import convert_output_pico_potentiometer
from _pins import PIN_LED

pinLED = Pin(PIN_LED, Pin.OUT)

while True:
    CMD = input("Enter a command (ON/OFF/TOGGLE): ")
    if CMD == "ON":
        pinLED.value(1)
    elif CMD == "OFF":
        pinLED.value(0)
    elif CMD == "TOGGLE":
        pinLED.toggle()
    else:
        print("Invalid command.")
    print("LED state: ", pinLED.value())
print("Finished.")
