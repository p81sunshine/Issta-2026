from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_volume_sphere_base():
    result = volume_sphere(10)
    expected = 4188.790204786391
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_sphere(25)
    expected = 65449.84694978735
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_sphere(20)
    expected = 33510.32163829113
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
