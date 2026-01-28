from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_extract_index_list_base():
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 7]
    assert extract_index_list([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 6, 5], [0, 1, 2, 3, 4, 6, 7]) == [1, 6]
    assert extract_index_list([1, 1, 3, 4, 6, 5, 6], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == [1, 5]
    assert extract_index_list([1, 2, 3, 4, 6, 6, 6], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7]) == []
