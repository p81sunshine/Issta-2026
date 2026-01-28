def swap_numbers(a, b):
    return (a, b)

# Test Cases (Partial...):
from solution import *

import math

import numpy as np
def test_swap_numbers_base():
    assert swap_numbers(10, 20) == (20, 10)
    assert swap_numbers(15, 17) == (17, 15)
    assert swap_numbers(100, 200) == (200, 100)