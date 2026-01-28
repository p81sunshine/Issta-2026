from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_rescale_to_unit_base():
    result = rescale_to_unit([2.0, 49.9])
    expected = [0.0, 1.0]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = rescale_to_unit([100.0, 49.9])
    expected = [1.0, 0.0]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = rescale_to_unit([2.0, 1.0, 5.0, 3.0, 4.0])
    expected = [0.25, 0.0, 1.0, 0.5, 0.75]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = rescale_to_unit([12.0, 11.0, 15.0, 13.0, 14.0])
    expected = [0.25, 0.0, 1.0, 0.5, 0.75]
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
