from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_div_list_base():
    result = div_list([4, 5, 6], [1, 2, 3])
    expected = [4.0, 2.5, 2.0]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = div_list([3, 2], [1, 4])
    expected = [3.0, 0.5]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = div_list([90, 120], [50, 70])
    expected = [1.8, 1.7142857142857142]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
