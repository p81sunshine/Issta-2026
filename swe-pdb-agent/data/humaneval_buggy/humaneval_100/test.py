from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_make_a_pile_base():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]
