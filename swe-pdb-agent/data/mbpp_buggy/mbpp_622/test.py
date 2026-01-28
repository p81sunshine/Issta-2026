from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_get_median_base():
    result = get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5)
    expected = 16.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = get_median([2, 4, 8, 9], [7, 13, 19, 28], 4)
    expected = 8.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6)
    expected = 25.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
