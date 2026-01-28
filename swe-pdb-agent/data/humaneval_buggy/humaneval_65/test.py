from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_circular_shift_base():
    assert circular_shift(100, 2) == '001'
    assert circular_shift(12, 2) == '12'
    assert circular_shift(97, 8) == '79'
    assert circular_shift(12, 1) == '21'
    assert circular_shift(11, 101) == '11'
