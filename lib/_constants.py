PICO = {
    "VOLTAGE": 3.3,
    # ...more constants
}

PICO_MIN_VOLTAGE = 0
PICO_MAX_VOLTAGE = 3.3

# PWM (Pulse Width Modulation) (analog output)
PICO_MIN_PWM_ACTUAL = 224  # q: where does 224 come from? # a: 224 is the minimum value of the PWM signal that can be used to turn on the LED (the LED turns on at 224 and above)
PICO_MIN_PWM = 0
PICO_MAX_PWM = 65535
# q: where does 65535 come from? # a: 2^16 - 1 = 65535 (65535 is the maximum value of a 16-bit unsigned integer) ("- 1" because the PWM signal can have 0 as a value, so the maximum value is 65535)
# q: where does the 16-bit unsigned integer come from? # a: the Pico has a 16-bit PWM resolution
