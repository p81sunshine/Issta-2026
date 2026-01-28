from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_volume_cylinder_base():
    result = volume_cylinder(10, 5)
    expected = 1570.7963267948967
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cylinder(4, 5)
    expected = 251.32741228718345
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cylinder(4, 10)
    expected = 502.6548245743669
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
