from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_max_base():
    assert find_max(['name', 'of', 'string']) == 'string'
    assert find_max(['name', 'enam', 'game']) == 'enam'
    assert find_max(['aaaaaaa', 'bb', 'cc']) == 'aaaaaaa'
    assert find_max(['abc', 'cba']) == 'abc'
    assert find_max(['play', 'this', 'game', 'of', 'footbott']) == 'footbott'
    assert find_max(['we', 'are', 'gonna', 'rock']) == 'gonna'
    assert find_max(['we', 'are', 'a', 'mad', 'nation']) == 'nation'
    assert find_max(['this', 'is', 'a', 'prrk']) == 'this'
    assert find_max(['b']) == 'b'
    assert find_max(['play', 'play', 'play']) == 'play'
