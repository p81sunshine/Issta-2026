from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_all_prefixes_base():
    assert all_prefixes('') == []
    assert all_prefixes('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert all_prefixes('WWW') == ['W', 'WW', 'WWW']
