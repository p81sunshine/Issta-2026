from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_will_it_fly_base():
    assert will_it_fly([3, 2, 3], 9) == True
    assert will_it_fly([1, 2], 5) == False
    assert will_it_fly([3], 5) == True
    assert will_it_fly([3, 2, 3], 1) == False
    assert will_it_fly([1, 2, 3], 6) == False
    assert will_it_fly([5], 5) == True
