from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_nth_nums_base():
    assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert nth_nums([10, 20, 30], 3) == [1000, 8000, 27000]
    assert nth_nums([12, 15], 5) == [248832, 759375]
