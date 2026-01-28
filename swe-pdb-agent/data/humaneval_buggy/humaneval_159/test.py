from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_eat_base():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(4, 5, 7) == [9, 2]
    assert eat(4, 5, 1) == [5, 0]
