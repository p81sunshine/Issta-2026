from solution import *

def test_example_1():
    assert canWinNim(4) is False, "Failed for n=4: expected False but got True"

def test_example_2():
    assert canWinNim(1) is True, "Failed for n=1: expected True but got False"

def test_example_3():
    assert canWinNim(2) is True, "Failed for n=2: expected True but got False"

def test_case_n3():
    assert canWinNim(3) is True, "Failed for n=3: expected True but got False"

def test_case_n8():
    assert canWinNim(8) is False, "Failed for n=8: expected False but got True"