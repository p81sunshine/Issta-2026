from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_histogram_base():
    assert histogram('a b b a') == {'a': 2, 'b': 2}
    assert histogram('a b c a b') == {'a': 2, 'b': 2}
    assert histogram('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}
    assert histogram('b b b b a') == {'b': 4}
    assert histogram('r t g') == {'r': 1, 't': 1, 'g': 1}
    assert histogram('') == {}
    assert histogram('a') == {'a': 1}
