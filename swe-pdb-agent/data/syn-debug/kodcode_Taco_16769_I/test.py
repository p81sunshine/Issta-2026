from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import minimum_adjacent_swaps

def test_example():
    assert minimum_adjacent_swaps([4, 3, 2, 1, 5, 6]) == 6

def test_sorted_list():
    assert minimum_adjacent_swaps([1, 2, 3, 4, 5, 6]) == 0

def test_reversed_list():
    assert minimum_adjacent_swaps([6, 5, 4, 3, 2, 1]) == 15

def test_mixed_list_1():
    assert minimum_adjacent_swaps([3, 1, 2]) == 2

def test_mixed_list_2():
    assert minimum_adjacent_swaps([1, 5, 3, 2, 4]) == 4

def test_single_element():
    assert minimum_adjacent_swaps([1]) == 0

def test_two_elements_sorted():
    assert minimum_adjacent_swaps([1, 2]) == 0

def test_two_elements_unsorted():
    assert minimum_adjacent_swaps([2, 1]) == 1