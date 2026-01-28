from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_sorted_base():
    assert is_sorted([5]) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([3, 2, 1]) == False
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False
    assert is_sorted([1, 2, 3, 3, 3, 4]) == False
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert is_sorted([1, 2, 3, 4]) == True
