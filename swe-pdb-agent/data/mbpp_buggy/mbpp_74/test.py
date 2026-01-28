from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_samepatterns_base():
    assert is_samepatterns(['red', 'green', 'green'], ['a', 'b', 'b']) == True
    assert is_samepatterns(['red', 'green', 'greenn'], ['a', 'b', 'b']) == False
    assert is_samepatterns(['red', 'green', 'greenn'], ['a', 'b']) == False
