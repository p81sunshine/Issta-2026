from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_extract_rear_base():
    assert extract_rear(['Mers', 'for', 'Vers']) == ['s', 'r', 's']
    assert extract_rear(['Avenge', 'for', 'People']) == ['e', 'r', 'e']
    assert extract_rear(['Gotta', 'get', 'go']) == ['a', 't', 'o']
