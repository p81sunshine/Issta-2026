from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_lateralsurface_cone_base():
    result = lateralsurface_cone(5, 12)
    expected = 204.20352248333654
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = lateralsurface_cone(10, 15)
    expected = 566.3586699569488
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = lateralsurface_cone(19, 17)
    expected = 1521.8090132193388
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
