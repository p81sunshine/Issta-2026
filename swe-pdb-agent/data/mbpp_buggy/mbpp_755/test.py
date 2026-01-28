from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_second_smallest_base():
    assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
    result = second_smallest([1, 1, -0.5, 0, 2, -2, -2])
    expected = -0.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert second_smallest([2, 2]) == None
    assert second_smallest([2, 2, 2]) == None
