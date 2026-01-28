import pytest
from acecode_evol_1504_llama3_1_instruct_39_code import common

def test_case_0():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]

def test_case_1():
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]

def test_case_2():
    assert common([-2, -3, 0, 2, 5], [-5, 2, 0, -3]) == [-3, 0, 2]

def test_case_3():
    assert common([], [1, 2, 3]) == []

def test_case_4():
    assert common([1, 2, 3], []) == []

def test_case_5():
    assert common([1, 2, 2, 3], [3, 3, 4]) == [3]

def test_case_6():
    assert common([-1, -2, 0, 1], [0, 1, 1, 2]) == [0, 1]

def test_case_7():
    assert common([10, 20, 30], [30, 20, 10]) == [10, 20, 30]

def test_case_8():
    assert common([1, 5, 3, 7], [2, 4, 6, 8]) == []

def test_case_9():
    assert common([-10, -20, -30], [-30, -10, -20]) == [-30, -20, -10]

def test_case_10():
    assert common([0, 0, 0], [0]) == [0]

def test_case_11():
    assert common([3, 5, 7, 9], [14, 5, 3]) == [3, 5]

def test_case_12():
    assert common([1, 1, 1, 1], [1]) == [1]

def test_case_13():
    assert common([-1, -1, -1], [-1]) == [-1]

def test_case_14():
    assert common([10, 9, 8], [8, 9, 10]) == [8, 9, 10]

def test_case_15():
    assert common([5, 1, 2], [2, 3, 1]) == [1, 2]

def test_case_16():
    assert common([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_case_17():
    assert common([100, 200, 300], [400, 500]) == []

def test_case_18():
    assert common([1, 2, 3, 3, 3], [3, 4, 5]) == [3]

def test_case_19():
    assert common([11, 12, 13], [14, 15, 16]) == []