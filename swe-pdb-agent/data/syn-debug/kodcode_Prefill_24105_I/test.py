from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import maximum_sum_subarray_2d

def test_empty_matrix():
    assert maximum_sum_subarray_2d([]) == 0

def test_single_element_matrix():
    assert maximum_sum_subarray_2d([[5]]) == 5
    assert maximum_sum_subarray_2d([[-3]]) == -3

def test_positive_elements_matrix():
    assert maximum_sum_subarray_2d([[1, 2], [3, 4]]) == 10

def test_negative_elements_matrix():
    assert maximum_sum_subarray_2d([[-1, -2], [-3, -4]]) == -1

def test_mixed_elements_matrix():
    assert maximum_sum_subarray_2d([[1, -2, 3], [-1, 4, -2], [3, -1, 2]]) == 7

def test_large_matrix():
    matrix = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]
    assert maximum_sum_subarray_2d(matrix) == 29