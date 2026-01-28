from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_radian_degree_base():
    result = radian_degree(90)
    expected = 1.5707963267948966
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = radian_degree(60)
    expected = 1.0471975511965976
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = radian_degree(120)
    expected = 2.0943951023931953
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
