from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import bubble_sort, insertion_sort, quick_sort, merge_sort, benchmark_sorts

def test_bubble_sort():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_insertion_sort():
    assert insertion_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]

def test_quick_sort():
    assert quick_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_merge_sort():
    assert merge_sort([8, 4, 2, 1]) == [1, 2, 4, 8]
    assert merge_sort([3, 7, 5, 2, 4, 6]) == [2, 3, 4, 5, 6, 7]

def test_benchmark_sorts():
    results = benchmark_sorts(100)  # Using smaller dataset for testing
    assert set(results.keys()) == {"bubble_sort", "insertion_sort", "quick_sort", "merge_sort"}
    for time in results.values():
        assert isinstance(time, float)
        assert time >= 0