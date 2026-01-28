from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_by_length_base():
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert by_length([]) == []
    assert by_length([1, -1, 55]) == ['One']
    assert by_length([1, -1, 3, 2]) == ['Three', 'Two', 'One']
    assert by_length([9, 4, 8]) == ['Nine', 'Eight', 'Four']
