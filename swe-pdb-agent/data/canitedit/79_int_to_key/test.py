from solution import *
import math

def test_all():
    encoder0 = LowerAlphaEncoder()
    encoder1 = UpperAlphaEncoder()
    encoder2 = UpperAlphaNumericEncoder()
    n0 = 0
    assert encoder0.encode(n0) == ""
    assert encoder1.encode(n0) == ""
    assert encoder2.encode(n0) == ""

    n1 = 1
    assert encoder0.encode(n1) == "a"
    assert encoder1.encode(n1) == "A"
    assert encoder2.encode(n1) == "A"

    n2 = 13
    assert encoder0.encode(n2) == "m"
    assert encoder1.encode(n2) == "M"
    assert encoder2.encode(n2) == "M"

    n3 = 26
    assert encoder0.encode(n3) == "z"
    assert encoder1.encode(n3) == "Z"
    assert encoder2.encode(n3) == "Z"

    n4 = 27
    assert encoder0.encode(n4) == "aa"
    assert encoder1.encode(n4) == "AA"
    assert encoder2.encode(n4) == "0A"

    n5 = 23623
    assert encoder0.encode(n5) == "ahxo"
    assert encoder1.encode(n5) == "AHXO"
    assert encoder2.encode(n5) == "H97O"