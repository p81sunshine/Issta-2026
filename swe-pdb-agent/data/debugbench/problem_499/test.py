from solution import *

def test_example_1():
    assert countGoodNumbers(1) == 5, "Failed for n=1: expected 5"

def test_example_2():
    assert countGoodNumbers(4) == 400, "Failed for n=4: expected 400"

def test_example_3():
    assert countGoodNumbers(50) == 564908303, "Failed for n=50: expected 564908303"

def test_case_n_2():
    assert countGoodNumbers(2) == 20, "Failed for n=2: expected 20"

def test_case_n_3():
    assert countGoodNumbers(3) == 100, "Failed for n=3: expected 100"