from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_even_odd_count_base():
    assert even_odd_count(7) == (0, 1)
    assert even_odd_count(-78) == (1, 1)
    assert even_odd_count(3452) == (2, 2)
    assert even_odd_count(346211) == (3, 3)
    assert even_odd_count(-345821) == (3, 3)
    assert even_odd_count(-2) == (1, 0)
    assert even_odd_count(-45347) == (2, 3)
    assert even_odd_count(0) == (1, 0)
