from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import min_swaps_to_sort_sequence

def test_example_case():
    assert min_swaps_to_sort_sequence(5, 3, [4, 3, 2, 1, 5]) == 2

def test_no_swaps_needed():
    assert min_swaps_to_sort_sequence(3, 1, [1, 2, 3]) == 0

def test_single_element():
    assert min_swaps_to_sort_sequence(1, 5, [1]) == 0

def test_impossible_to_sort():
    assert min_swaps_to_sort_sequence(4, 1, [4, 1, 3, 2]) == -1

def test_already_sorted():
    assert min_swaps_to_sort_sequence(5, 3, [1, 2, 3, 4, 5]) == 0

def test_large_k_value():
    assert min_swaps_to_sort_sequence(5, 1000000, [4, 3, 2, 1, 5]) == 2

def test_disconnected_cycles():
    assert min_swaps_to_sort_sequence(6, 2, [6, 2, 4, 1, 3, 5]) == -1

if __name__ == '__main__':
    pytest.main()