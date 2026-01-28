from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_larg_nnum_base():
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5) == [100, 90, 80, 70, 60]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3) == [100, 90, 80]
