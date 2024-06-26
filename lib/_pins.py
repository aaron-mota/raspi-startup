#  PWM pins (https://www.youtube.com/watch?v=GXA1Y6lA14A&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=11&ab_channel=PaulMcWhorter)

# Options
# Pin() # (General Purpose Input/Output) # Digital Input/Output (e.g. button, LED, etc.)
# ADC() # (Analog Input) # Analog to Digital Converter (e.g. potentiometer, temperature sensor, etc.)
# PWM() # (Analog Output) # Pulse Width Modulation (e.g. LED brightness, motor speed, etc.)
# I2C() # (Digital Communication) # Inter-Integrated Circuit (e.g. sensor, display, etc.)
# SPI() # (Digital Communication) # Serial Peripheral Interface (e.g. sensor, display, etc.)
# Timer() # (Digital Communication) # Software timer (e.g. blinking LED, etc.)


# Full source of truth for given GP pin
PIN_GP0__1__SPI0_RX__I2C0_SDA__UART1_TX = 0
PIN_GP1__2__SPI0_CSn__I2C0_SCL__UART1_RX = 1
PIN_GP2__4__SPI0_SCK__I2C1_SDA = 2
PIN_GP3__5__SPI0_TX__I2C1_SCL = 3
PIN_GP4__6__SPI0_RX__I2C0_SDA__UART1_TX = 4
PIN_GP5__7__SPI0_CSn__I2C0_SCL__UART1_RX = 5
PIN_GP6__9__SPI0_SCK__I2C1_SDA = 6
PIN_GP7__10__SPI0_TX__I2C1_SCL = 7
PIN_GP8__11__SPI1_RX__I2C0_SDA__UART1_TX = 8
PIN_GP9__12__SPI1_CSn__I2C0_SCL__UART1_RX = 9
PIN_GP10__14__SPI1_SCK__I2C1_SDA = 10
PIN_GP11__15__SPI1_TX__I2C1_SCL = 11
PIN_GP12__16__SPI1_RX__I2C0_SDA__UART1_TX = 12
PIN_GP13__17__SPI1_CSn__I2C0_SCL__UART1_RX = 13
PIN_GP14__19__SPI1_SCK__I2C1_SDA = 14
PIN_GP15__20__SPI1_TX__I2C1_SCL = 15

PIN_GP16__21_20b__SPI0_RX__I2C0_SDA__UART1_TX = 16
PIN_GP17__22_19b__SPI0_CSn__I2C0_SCL__UART1_RX = 17
PIN_GP18__24_17b__SPI0_SCK__I2C1_SDA = 18
PIN_GP19__25_16b__SPI0_TX__I2C1_SCL = 19
PIN_GP20__26_15b__I2C0_SDA = 19
PIN_GP21__27_14b__I2C0_SCL = 20
PIN_GP22__29_12b = 21
PIN_GP26__31_10b__ADC0__I2C1_SDA = 26
PIN_GP27__32_9b__ADC1__I2C1_SCL = 27
PIN_GP28__34_7b__ADC2 = 28

#####
# Context-specific constants
#####
## GPIO (General Purpose Input/Output)
PIN_GP0__1 = 0
PIN_GP1__2 = 1
PIN_GP2__4 = 2
PIN_GP3__5 = 3
PIN_GP4__6 = 4
PIN_GP5__7 = 5
PIN_GP6__9 = 6
PIN_GP7__10 = 7
PIN_GP8__11 = 8
PIN_GP9__12 = 9
PIN_GP10__14 = 10
PIN_GP11__15 = 11
PIN_GP12__16 = 12
PIN_GP13__17 = 13
PIN_GP14__19 = 14
PIN_GP15__20 = 15
PIN_GP16__21_20b = 16
PIN_GP17__22_19b = 17
PIN_GP18__24_17b = 18
PIN_GP19__25_16b = 19
PIN_GP20__26_15b = 20
PIN_GP21__27_14b = 21
PIN_GP22__29_12b = 22
PIN_GP26__31_10b = 26
PIN_GP27__32_9b = 27
PIN_GP28__34_7b = 28

## ADC (Analog to Digital Converter)
# PIN_ADC0__31_10b = 26
# PIN_ADC1__32_9b = 27
# PIN_ADC2__34_7b = 28

## SPI (Serial Peripheral Interface)
# PIN_SPI0_RX__21_20b = 0
# PIN_SPI0_CSn__22_19b = 1
# PIN_SPI0_SCK__24_17b = 2
# PIN_SPI0_TX__25_16b = 3
# PIN_SPI0_RX__26_15b = 4
# PIN_SPI0_CSn__27_14b = 5
# PIN_SPI0_SCK__29_12b = 6
# PIN_SPI0_TX__31_10b = 7
# PIN_SPI1_RX__21_20b = 8
# PIN_SPI1_CSn__22_19b = 9
# PIN_SPI1_SCK__24_17b = 10
# PIN_SPI1_TX__25_16b = 11
# PIN_SPI1_RX__26_15b = 12
# PIN_SPI1_CSn__27_14b = 13
# PIN_SPI1_SCK__29_12b = 14
# PIN_SPI1_TX__31_10b = 15

## I2C (Inter-Integrated Circuit)
# PIN_I2C0_SDA__26_15b = 19
# PIN_I2C0_SCL__27_14b = 20
# PIN_I2C1_SDA__24_17b = 21
# PIN_I2C1_SCL__25_16b = 22
# PIN_I2C1_SDA__31_10b = 26
# PIN_I2C1_SCL__32_9b = 27

## UART (Universal Asynchronous Receiver-Transmitter)
# PIN_UART1_TX__21_20b = 0
# PIN_UART1_RX__22_19b = 1
# PIN_UART1_TX__26_15b = 2
# PIN_UART1_RX__27_14b = 3

## OTHER
PIN_LED = "LED"  # LED (internal component)
PIN_VBUS__40_1b = False  # USB power
PIN_VSYS__39_2b = False  # System power
PIN_3V3_EN__37_4b = False  # 3.3V power (enable)
PIN_3V3_OUT__36_5b = False  # 3.3V power (output)
PIN_RUN__30_11b = False  # Reset (?)
PIN_GND__3 = False  # Ground
PIN_GND__8 = False
PIN_GND__13 = False
PIN_GND__18 = False
PIN_GND__23_18b = False
PIN_GND__28_13b = False
PIN_GND__33_8b = False
PIN_GND__38_3b = False
