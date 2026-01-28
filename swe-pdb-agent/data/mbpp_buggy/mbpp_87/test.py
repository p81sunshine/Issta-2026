from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_merge_dictionaries_three_base():
    assert merge_dictionaries_three({'R': 'Red', 'P': 'Pink'}, {'G': 'Green'}, {'O': 'Orange', 'W': 'White', 'B': 'Black'}) == {'O': 'Orange', 'W': 'White', 'B': 'Black', 'G': 'Green', 'R': 'Red', 'P': 'Pink'}
    assert merge_dictionaries_three({'R': 'Red', 'P': 'Pink'}, {'G': 'Green', 'W': 'White'}, {'L': 'lavender', 'B': 'Blue'}) == {'L': 'lavender', 'B': 'Blue', 'G': 'Green', 'W': 'White', 'R': 'Red', 'P': 'Pink'}
    assert merge_dictionaries_three({'R': 'Red', 'P': 'Pink'}, {'L': 'lavender', 'B': 'Blue'}, {'G': 'Green', 'W': 'White'}) == {'G': 'Green', 'W': 'White', 'L': 'lavender', 'B': 'Blue', 'R': 'Red', 'P': 'Pink'}
