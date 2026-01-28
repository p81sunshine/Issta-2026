from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_lateralsuface_cylinder_base():
    result = lateralsuface_cylinder(10, 5)
    expected = 314.1592653589793
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = lateralsuface_cylinder(4, 5)
    expected = 125.66370614359172
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = lateralsuface_cylinder(4, 10)
    expected = 251.32741228718345
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
