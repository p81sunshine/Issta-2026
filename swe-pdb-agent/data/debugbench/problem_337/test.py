from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False

def test_n_zero():
    assert canPlaceFlowers([1,0,0], 0) is True

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True

def test_two_zeros():
    assert canPlaceFlowers([0,0], 1) is True