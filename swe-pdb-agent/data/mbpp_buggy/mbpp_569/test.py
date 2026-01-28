from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_sort_sublists_base():
    assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]) == [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    assert sort_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']]) == [['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
    assert sort_sublists([['a', 'b'], ['d', 'c'], ['g', 'h'], ['f', 'e']]) == [['a', 'b'], ['c', 'd'], ['g', 'h'], ['e', 'f']]
