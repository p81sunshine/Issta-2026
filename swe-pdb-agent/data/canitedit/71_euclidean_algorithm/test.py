from solution import *
import math

def test_all():
    assert gcd(30, 10) == 10
    assert gcd(63, 81) == 9
    assert gcd(99, 121) == 11
    assert gcd(2, 2) == 2
    assert gcd(48, 60) == 12

    assert lcm(81, 108) == 324
    assert lcm(63, 81) == 567
    assert lcm(12, 18) == 36
    assert lcm(4, 6) == 12
    assert lcm(3, 8) == 24