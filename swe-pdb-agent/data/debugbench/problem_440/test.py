from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") == True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") == True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") == False, "Example 3 should return False"

def test_same_strings():
    assert isTransformable("12345", "12345") == True, "Identical strings should return True"

def test_reverse_case():
    assert isTransformable("21", "12") == True, "Simple reverse case should return True"