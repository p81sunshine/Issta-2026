from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_average_tuple_base():
    result = average_tuple([[10, 10, 10, 12], [30, 45, 56, 45], [81, 80, 39, 32], [1, 2, 3, 4]])
    expected = [30.5, 34.25, 27.0, 23.25]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = average_tuple([[1, 1, -5], [30, -15, 56], [81, -60, -39], [-10, 2, 3]])
    expected = [25.5, -18.0, 3.75]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = average_tuple([[100, 100, 100, 120], [300, 450, 560, 450], [810, 800, 390, 320], [10, 20, 30, 40]])
    expected = [305.0, 342.5, 270.0, 232.5]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
