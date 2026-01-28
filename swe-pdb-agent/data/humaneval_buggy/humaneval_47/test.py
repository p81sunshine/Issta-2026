from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_median_base():
    assert median([3, 1, 2, 4, 5]) == 3
    result = median([-10, 4, 6, 1000, 10, 20])
    expected = 8.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert median([5]) == 5
    result = median([6, 5])
    expected = 5.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert median([8, 1, 3, 9, 9, 2, 7]) == 7
