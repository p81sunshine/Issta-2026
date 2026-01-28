from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_adverb_position_base():
    assert find_adverb_position('clearly!! we can see the sky') == (0, 7, 'clearly')
    assert find_adverb_position('seriously!! there are many roses') == (0, 9, 'seriously')
    assert find_adverb_position('unfortunately!! sita is going to home') == (0, 13, 'unfortunately')
