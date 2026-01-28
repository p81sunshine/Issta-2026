from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_extract_singly_base():
    assert extract_singly([[3, 4, 5], [4, 5, 7], [1, 4]]) == {1, 3, 4, 5, 7}
    assert extract_singly([[1, 2, 3], [4, 2, 3], [7, 8]]) == {1, 2, 3, 4, 7, 8}
    assert extract_singly([[7, 8, 9], [10, 11, 12], [10, 11]]) == {7, 8, 9, 10, 11, 12}
