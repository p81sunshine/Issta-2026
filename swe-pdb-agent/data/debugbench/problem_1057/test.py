from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") == True, "Example 1 failed"

def test_example_2():
    assert isTransformable("34521", "23415") == True, "Example 2 failed"

def test_example_3():
    assert isTransformable("12345", "12435") == False, "Example 3 failed"

def test_additional_case():
    assert isTransformable("123", "132") == False, "Additional test case failed"