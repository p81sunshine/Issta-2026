from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_mean_absolute_deviation_base():
    result = mean_absolute_deviation([1.0, 2.0, 3.0])
    expected = 0.6666666666666666
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    expected = 1.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = 1.2
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
