from machine import Pin
from utime import sleep

pinLED = Pin("LED", Pin.OUT)
pin15 = Pin(15, Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin15.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin15.off()
print("Finished.")

