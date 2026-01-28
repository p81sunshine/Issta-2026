from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_below_threshold_base():
    assert below_threshold([1, 2, 4, 10], 100) == True
    assert below_threshold([1, 20, 4, 10], 5) == False
    assert below_threshold([1, 20, 4, 10], 21) == True
    assert below_threshold([1, 20, 4, 10], 22) == True
    assert below_threshold([1, 8, 4, 10], 11) == True
    assert below_threshold([1, 8, 4, 10], 10) == False
