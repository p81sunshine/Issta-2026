from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_Average_Of_Cube_base():
    result = find_Average_Of_Cube(2)
    expected = 4.5
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = find_Average_Of_Cube(3)
    expected = 12.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = find_Average_Of_Cube(1)
    expected = 1.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
