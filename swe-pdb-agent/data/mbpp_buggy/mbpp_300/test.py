from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_count_binary_seq_base():
    result = count_binary_seq(1)
    expected = 2.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = count_binary_seq(2)
    expected = 6.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = count_binary_seq(3)
    expected = 20.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
