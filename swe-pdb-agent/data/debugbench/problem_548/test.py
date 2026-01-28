from solution import *

def test_example_1():
    assert findComplement(5) == 2, "Test case 1 failed: num=5 should return 2"

def test_example_2():
    assert findComplement(1) == 0, "Test case 2 failed: num=1 should return 0"

def test_additional_case():
    assert findComplement(7) == 0, "Test case 3 failed: num=7 should return 0"

def test_edge_case_two():
    assert findComplement(2) == 1, "Test case 4 failed: num=2 should return 1"