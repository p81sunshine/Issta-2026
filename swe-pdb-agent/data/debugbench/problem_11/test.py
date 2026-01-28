from solution import *

def test_example_1():
    assert minimumDeletions([2,10,7,5,4,1,8,6]) == 5, "Failed for example 1"

def test_example_2():
    assert minimumDeletions([0,-4,19,1,8,-2,-3,5]) == 3, "Failed for example 2"

def test_example_3():
    assert minimumDeletions([101]) == 1, "Failed for single-element case"

def test_additional_case():
    assert minimumDeletions([3,1,4,2]) == 3, "Failed for reordered min/max indices case"