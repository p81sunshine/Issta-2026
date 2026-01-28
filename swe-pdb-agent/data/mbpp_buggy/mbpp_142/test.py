from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_count_samepair_base():
    assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9]) == 3
    assert count_samepair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8]) == 4
    assert count_samepair([1, 2, 3, 4, 2, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8]) == 5
