from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_drop_empty_base():
    assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}) == {'c1': 'Red', 'c2': 'Green'}
    assert drop_empty({'c1': 'Red', 'c2': None, 'c3': None}) == {'c1': 'Red'}
    assert drop_empty({'c1': None, 'c2': 'Green', 'c3': None}) == {'c2': 'Green'}
