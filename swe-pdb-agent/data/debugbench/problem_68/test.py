from solution import *
import pytest


def test_example_1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    result = median_sliding_window(nums, k)
    assert result == pytest.approx(expected), f"Example 1 failed: {result} != {expected}"


def test_example_2():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    result = median_sliding_window(nums, k)
    assert result == pytest.approx(expected), f"Example 2 failed: {result} != {expected}"


def test_even_window_average():
    nums = [1, 3, 2, 4]
    k = 2
    expected = [2.0, 2.5, 3.0]
    result = median_sliding_window(nums, k)
    assert result == pytest.approx(expected), f"Even window average test failed: {result} != {expected}"


def test_single_element_window():
    nums = [5]
    k = 1
    expected = [5.0]
    result = median_sliding_window(nums, k)
    assert result == pytest.approx(expected), f"Single element window test failed: {result} != {expected}"


def test_all_elements_same_even_k():
    nums = [5, 5, 5, 5]
    k = 2
    expected = [5.0, 5.0, 5.0]
    result = median_sliding_window(nums, k)
    assert result == pytest.approx(expected), f"All elements same test failed: {result} != {expected}"