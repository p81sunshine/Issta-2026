import pytest
from acecode_evol_9766_llama3_1_instruct_37_code import find_median

def test_case_0():
    assert find_median([5, 3, 9, 7, 1]) == 5.0

def test_case_1():
    assert find_median([1, 2, 3, 4, 5]) == 3.0

def test_case_2():
    assert find_median([3, 1, 2]) == 2.0

def test_case_3():
    assert find_median([4, 1, 7, 2]) == 3.0

def test_case_4():
    assert find_median([-1, -3, -2]) == -2.0

def test_case_5():
    assert find_median([0, 0, 0, 0]) == 0.0

def test_case_6():
    assert find_median([10, 20, 30, 40]) == 25.0

def test_case_7():
    assert find_median([1]) == 1.0

def test_case_8():
    assert find_median([-10, -100, 0, 100]) == -5.0

def test_case_9():
    assert find_median([2, 8, 5, 4]) == 4.5

def test_case_10():
    assert find_median([7, 7, 7, 7, 7]) == 7.0

def test_case_11():
    assert find_median([1, 2]) == 1.5

def test_case_12():
    assert find_median([3, 5, 1, 9, 7]) == 5.0

def test_case_13():
    assert find_median([-5, -2, -3, -4]) == -3.5

def test_case_14():
    assert find_median([1, 3, 3, 6, 7, 8, 9]) == 6.0

def test_case_15():
    assert find_median([1, 1, 1, 1, 1, 1, 1, 1]) == 1.0

def test_case_16():
    assert find_median([-1, -2, -3]) == -2.0

def test_case_17():
    assert find_median([100, 200, 300, 400]) == 250.0

def test_case_18():
    assert find_median([2, 3, 4, 5, 6]) == 4.0

def test_case_19():
    assert find_median([1, 2, 2, 2, 3]) == 2.0