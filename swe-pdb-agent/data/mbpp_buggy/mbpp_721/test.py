from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_maxAverageOfPath_base():
    result = maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]])
    expected = 5.2
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]])
    expected = 6.2
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]])
    expected = 7.2
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected = 5.8
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
