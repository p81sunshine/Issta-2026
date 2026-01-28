import pytest
from acecode_evol_16460_llama3_1_instruct_37_code import findMaxThree

def test_case_0():
    assert findMaxThree([3, 10, 2, 5, 9, 8, 33, 21, 1, 7]) == [33, 21, 10]

def test_case_1():
    assert findMaxThree([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [5]

def test_case_2():
    assert findMaxThree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8]

def test_case_3():
    assert findMaxThree([10, 9, 10, 9, 8, 8, 7, 6, 5, 4]) == [10, 9, 8]

def test_case_4():
    assert findMaxThree([7, 8, 9, 10, 10, 10, 8, 7, 6, 5]) == [10, 9, 8]

def test_case_5():
    assert findMaxThree([3, 2, 3, 1, 2, 4, 5, 5, 5, 5]) == [5, 4, 3]

def test_case_6():
    assert findMaxThree([15, 2, 9, 7, 15, 11, 4, 5, 6, 7]) == [15, 11, 9]

def test_case_7():
    assert findMaxThree([1, 2, 3, 1, 1, 1, 1, 1, 1, 1]) == [3, 2, 1]

def test_case_8():
    assert findMaxThree([8, 8, 8, 8, 8, 8, 8, 8, 8, 8]) == [8]

def test_case_9():
    assert findMaxThree([10, 9, 8, 10, 9, 8, 10, 9, 8, 7]) == [10, 9, 8]

def test_case_10():
    assert findMaxThree([5, 4, 3, 2, 1, 0, -1, -2, -3, -4]) == [5, 4, 3]

def test_case_11():
    assert findMaxThree([6, 6, 6, 6, 6, 6, 6, 6, 6, 6]) == [6]

def test_case_12():
    assert findMaxThree([7, 7, 8, 8, 9, 9, 10, 10, 10, 10]) == [10, 9, 8]

def test_case_13():
    assert findMaxThree([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [5, 4, 3]

def test_case_14():
    assert findMaxThree([11, 11, 11, 11, 10, 10, 10, 9, 9, 8]) == [11, 10, 9]

def test_case_15():
    assert findMaxThree([1, 2, 3, 3, 2, 1, 0, 0, 0, 0]) == [3, 2, 1]

def test_case_16():
    assert findMaxThree([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9, 8, 7]