from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_generate_integers_base():
    assert generate_integers(2, 10) == [2, 4, 6, 8]
    assert generate_integers(10, 2) == [2, 4, 6, 8]
    assert generate_integers(132, 2) == [2, 4, 6, 8]
    assert generate_integers(17, 89) == []
