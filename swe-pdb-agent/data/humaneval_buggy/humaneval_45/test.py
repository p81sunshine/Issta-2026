from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_triangle_area_base():
    result = triangle_area(5, 3)
    expected = 7.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = triangle_area(2, 2)
    expected = 2.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = triangle_area(10, 8)
    expected = 40.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
