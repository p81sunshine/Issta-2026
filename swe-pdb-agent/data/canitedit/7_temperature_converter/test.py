from solution import *
import math

def test_all():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37.3) == 99.14
    assert round(celsius_to_fahrenheit(-273.15), 2) == -459.67
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    assert round(fahrenheit_to_celsius(99.14), 2) == 37.3
    assert round(fahrenheit_to_celsius(-459.67), 2) == -273.15
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(30) == 86
    assert round(celsius_to_fahrenheit(21.11), 2) == 70
    assert round(celsius_to_fahrenheit(-17.78), 2) == 0