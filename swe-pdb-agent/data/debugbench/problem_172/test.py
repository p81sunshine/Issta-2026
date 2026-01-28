from solution import *

def test_example_1():
    assert canWinNim(4) is False, "Failed for n=4: should return False when n is multiple of 4"

def test_example_2():
    assert canWinNim(1) is True, "Failed for n=1: should return True when n is not multiple of 4"

def test_example_3():
    assert canWinNim(2) is True, "Failed for n=2: should return True when n is not multiple of 4"

def test_additional_case():
    assert canWinNim(3) is True, "Failed for n=3: should return True when n is not multiple of 4"