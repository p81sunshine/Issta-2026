def even_bit_set_number(n): 
    mask = 1
    while mask < n:
        n |= mask
        mask <<= 2
    return n

# Test Cases (Partial...):
from solution import *
import math
import numpy as np
def test_even_bit_set_number_base():
    assert even_bit_set_number(10) == 10
    assert even_bit_set_number(20) == 30
    assert even_bit_set_number(30) == 30