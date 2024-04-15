from machine import Pin
from utime import sleep
from _constants import PIN_LED

pin = Pin(PIN_LED, Pin.OUT)

print("LED starts flashing...")
while True:
    try:
        pin.toggle()
        sleep(1) # sleep 1sec
    except KeyboardInterrupt:
        break
pin.off()
print("Finished.")


# For access to the hardware use the 'machine' module.  RP2 specific commands
# are in the 'rp2' module.

# Quick overview of some objects:
#   machine.Pin(pin) -- get a pin, eg machine.Pin(0)
#   machine.Pin(pin, m, [p]) -- get a pin and configure it for IO mode m, pull mode p
#     methods: init(..), value([v]), high(), low(), irq(handler)
#   machine.ADC(pin) -- make an analog object from a pin
#     methods: read_u16()
#   machine.PWM(pin) -- make a PWM object from a pin
#     methods: deinit(), freq([f]), duty_u16([d]), duty_ns([d])
#   machine.I2C(id) -- create an I2C object (id=0,1)
#     methods: readfrom(addr, buf, stop=True), writeto(addr, buf, stop=True)
#              readfrom_mem(addr, memaddr, arg), writeto_mem(addr, memaddr, arg)
#   machine.SPI(id, baudrate=1000000) -- create an SPI object (id=0,1)
#     methods: read(nbytes, write=0x00), write(buf), write_readinto(wr_buf, rd_buf)
#   machine.Timer(freq, callback) -- create a software timer object
#     eg: machine.Timer(freq=1, callback=lambda t:print(t))

# Pins are numbered 0-29, and 26-29 have ADC capabilities
# Pin IO modes are: Pin.IN, Pin.OUT, Pin.ALT
# Pin pull modes are: Pin.PULL_UP, Pin.PULL_DOWN

# Useful control commands:
#   CTRL-C -- interrupt a running program
#   CTRL-D -- on a blank line, do a soft reset of the board
#   CTRL-E -- on a blank line, enter paste mode

# For further help on a specific object, type help(obj)
# For a list of available modules, type help('modules')
# None
# >>> 

