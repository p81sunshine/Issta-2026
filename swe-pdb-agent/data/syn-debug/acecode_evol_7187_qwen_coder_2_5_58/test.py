import pytest
from acecode_evol_7187_qwen_coder_2_5_58_code import combine_collections

def test_case_0():
    assert combine_collections([2, 4, 5, 6], [1, 2, 3, 4]) == [1, 2, 3, 4, 5, 6]

def test_case_1():
    assert combine_collections([-1, 0, 1], [1, 2, 3]) == [-1, 0, 1, 2, 3]

def test_case_2():
    assert combine_collections([], [5, 3, 1]) == [1, 3, 5]

def test_case_3():
    assert combine_collections([3, 3, 3], [2, 2, 2]) == [2, 3]

def test_case_4():
    assert combine_collections([-5, -1, 0], [0, 1, 5]) == [-5, -1, 0, 1, 5]

def test_case_5():
    assert combine_collections([10, 20, 30], [30, 40, 50]) == [10, 20, 30, 40, 50]

def test_case_6():
    assert combine_collections([1, 1, 1], [1, 1, 1]) == [1]

def test_case_7():
    assert combine_collections([100, 200], [-100, -200]) == [-200, -100, 100, 200]

def test_case_8():
    assert combine_collections([0, 0, 0], [0, 0, 0]) == [0]

def test_case_9():
    assert combine_collections([7, 5, 3], [2, 1, 4]) == [1, 2, 3, 4, 5, 7]

def test_case_10():
    assert combine_collections([2, 2, 2], [3, 3, 3]) == [2, 3]

def test_case_11():
    assert combine_collections([-10, -20, -30], [-10, -5, -20]) == [-30, -20, -10, -5]

def test_case_12():
    assert combine_collections([1, 2, 3], []) == [1, 2, 3]

def test_case_13():
    assert combine_collections([], []) == []

def test_case_14():
    assert combine_collections([-1, -2, -3], [3, 2, 1]) == [-3, -2, -1, 1, 2, 3]

def test_case_15():
    assert combine_collections([0], [-1, 1]) == [-1, 0, 1]

def test_case_16():
    assert combine_collections([4, 4, 4], []) == [4]

def test_case_17():
    assert combine_collections([6, -2, 3], [4, 0, -2]) == [-2, 0, 3, 4, 6]

def test_case_18():
    assert combine_collections([-1, -1, -1, -2], [-2, -3, -3]) == [-3, -2, -1]

def test_case_19():
    assert combine_collections([1000000000, 999999999], [999999998, 1000000000]) == [999999998, 999999999, 1000000000]