from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_is_bored_base():
    assert is_bored('Hello world') == 0
    assert is_bored('Is the sky blue?') == 0
    assert is_bored('I love It !') == 1
    assert is_bored('bIt') == 0
    assert is_bored('I feel good today. I will be productive. will kill It') == 2
    assert is_bored('You and I are going for a walk') == 0
