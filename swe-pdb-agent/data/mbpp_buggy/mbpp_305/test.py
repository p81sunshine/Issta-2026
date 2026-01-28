from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_start_withp_base():
    assert start_withp(['Python PHP', 'Java JavaScript', 'c c++']) == ('Python', 'PHP')
    assert start_withp(['Python Programming', 'Java Programming']) == ('Python', 'Programming')
    assert start_withp(['Pqrst Pqr', 'qrstuv']) == ('Pqrst', 'Pqr')
