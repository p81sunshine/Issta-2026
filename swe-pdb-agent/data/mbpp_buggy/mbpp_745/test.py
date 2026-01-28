from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_divisible_by_digits_base():
    assert divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1, 15) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20, 25) == [22, 24]
