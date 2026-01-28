from solution import *

def test_example_1():
    assert kthFactor(12, 3) == 3, "Failed for n=12, k=3"

def test_example_2():
    assert kthFactor(7, 2) == 7, "Failed for n=7, k=2"

def test_example_3():
    assert kthFactor(4, 4) == -1, "Failed for n=4, k=4"

def test_k_equals_1():
    assert kthFactor(5, 1) == 1, "Failed for k=1 case"

def test_edge_case_small_n():
    assert kthFactor(2, 2) == 2, "Failed for n=2, k=2"