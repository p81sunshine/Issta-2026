from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_triangle_area_base():
    result = triangle_area(3, 4, 5)
    expected = 6.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert triangle_area(1, 2, 10) == -1
    result = triangle_area(4, 8, 5)
    expected = 8.18
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = triangle_area(2, 2, 2)
    expected = 1.73
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert triangle_area(1, 2, 3) == -1
    result = triangle_area(10, 5, 7)
    expected = 16.25
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert triangle_area(2, 6, 3) == -1
    result = triangle_area(1, 1, 1)
    expected = 0.43
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    assert triangle_area(2, 2, 10) == -1
