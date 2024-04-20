from machine import Pin
from utime import sleep
from _pins import PIN_GP15__20 as PIN_GP15, PIN_LED

pinLED = Pin(PIN_LED, Pin.OUT)
pin15 = Pin(PIN_GP15, Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin15.toggle()
        sleep(1)  # sleep 1sec
    except KeyboardInterrupt:
        break
pin15.off()
print("Finished.")
