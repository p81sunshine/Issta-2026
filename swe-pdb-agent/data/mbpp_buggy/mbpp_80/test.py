from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_tetrahedral_number_base():
    result = tetrahedral_number(5)
    expected = 35.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = tetrahedral_number(6)
    expected = 56.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = tetrahedral_number(7)
    expected = 84.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
