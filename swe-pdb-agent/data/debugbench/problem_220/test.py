from solution import *

def test_example_1():
    assert maxValueAfterReverse([2, 3, 1, 5, 4]) == 10, "Example 1 should return 10"

def test_example_2():
    assert maxValueAfterReverse([2, 4, 9, 24, 2, 1, 10]) == 68, "Example 2 should return 68"

def test_custom_case():
    assert maxValueAfterReverse([1, 3, 2, 4]) == 6, "Custom test case should return 6"