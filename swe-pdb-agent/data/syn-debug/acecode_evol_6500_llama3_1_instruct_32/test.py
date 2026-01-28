import pytest
from acecode_evol_6500_llama3_1_instruct_32_code import find_common_elements

def test_case_0():
    assert find_common_elements([1, 2, 3], [4, 5, 6]) == []

def test_case_1():
    assert find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

def test_case_2():
    assert find_common_elements([1, 1, 2, 2], [2, 2, 3, 3]) == [2]

def test_case_3():
    assert find_common_elements([], [1, 2, 3]) == []

def test_case_4():
    assert find_common_elements([1, 2, 3], []) == []

def test_case_5():
    assert find_common_elements([5, 6, 7], [1, 2, 3]) == []

def test_case_6():
    assert find_common_elements([9, 10, 10, 11], [10, 11, 12, 13]) == [10, 11]

def test_case_7():
    assert find_common_elements([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_case_8():
    assert find_common_elements([1, 3, 5, 7], [2, 4, 6, 8]) == []

def test_case_9():
    assert find_common_elements([-1, -2, -3], [-3, -2, -1]) == [-3, -2, -1]

def test_case_10():
    assert find_common_elements([100, 200, 300], [300, 200, 100]) == [100, 200, 300]

def test_case_11():
    assert find_common_elements([4, 5, 6, 7, 8], [2, 3, 4, 5]) == [4, 5]

def test_case_12():
    assert find_common_elements([1, 2, 2], [2, 2, 3]) == [2]

def test_case_13():
    assert find_common_elements([10, 20, 30], [30, 40, 50]) == [30]

def test_case_14():
    assert find_common_elements([1, 2, 3, 4], [1, 1, 1, 1]) == [1]

def test_case_15():
    assert find_common_elements([0, 0, 0], [0, 0, 0]) == [0]

def test_case_16():
    assert find_common_elements([5, 5, 5, 5], [5, 5, 5, 5]) == [5]

def test_case_17():
    assert find_common_elements([1, 2, 3], [3, 3, 3]) == [3]

def test_case_18():
    assert find_common_elements([1, 2, 2, 3], [1, 1, 2]) == [1, 2]