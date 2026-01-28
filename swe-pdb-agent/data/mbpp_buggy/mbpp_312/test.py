from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_volume_cone_base():
    result = volume_cone(5, 12)
    expected = 314.15926535897927
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cone(10, 15)
    expected = 1570.7963267948965
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = volume_cone(19, 17)
    expected = 6426.651371693521
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
