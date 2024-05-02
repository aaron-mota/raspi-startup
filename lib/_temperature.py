def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def convert_celsius_to_kelvin(celsius):
    return celsius + 273.15


def convert_kelvin_to_fahrenheit(kelvin):
    return convert_celsius_to_fahrenheit(convert_kelvin_to_celsius(kelvin))


def convert_fahrenheit_to_kelvin(fahrenheit):
    return convert_celsius_to_kelvin(convert_fahrenheit_to_celsius(fahrenheit))
