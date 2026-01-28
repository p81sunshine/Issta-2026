from solution import *

def test_example_1():
    assert min_eating_speed([3,6,7,11], 8) == 4

def test_example_2():
    assert min_eating_speed([30,11,23,4,20], 5) == 30

def test_example_3():
    assert min_eating_speed([30,11,23,4,20], 6) == 23

def test_edge_single_pile():
    assert min_eating_speed([100], 1) == 100

def test_edge_large_h():
    assert min_eating_speed([5,5], 10) == 1