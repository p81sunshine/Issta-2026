from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_median_trapezium_base():
    result = median_trapezium(15, 25, 35)
    expected = 20.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = median_trapezium(10, 20, 30)
    expected = 15.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = median_trapezium(6, 9, 4)
    expected = 7.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
