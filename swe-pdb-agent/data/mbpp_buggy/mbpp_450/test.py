from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_extract_string_base():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 6) == ['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 9) == ['exercises']
