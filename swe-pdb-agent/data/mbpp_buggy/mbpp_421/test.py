from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_concatenate_tuple_base():
    assert concatenate_tuple(['ID', 'is', 4, 'UTS']) == 'ID-is-4-UTS'
    assert concatenate_tuple(['QWE', 'is', 4, 'RTY']) == 'QWE-is-4-RTY'
    assert concatenate_tuple(['ZEN', 'is', 4, 'OP']) == 'ZEN-is-4-OP'
