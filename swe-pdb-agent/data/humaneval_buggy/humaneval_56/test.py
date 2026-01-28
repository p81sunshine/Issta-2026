from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_correct_bracketing_base():
    assert correct_bracketing('<>') == True
    assert correct_bracketing('<<><>>') == True
    assert correct_bracketing('<><><<><>><>') == True
    assert correct_bracketing('<><><<<><><>><>><<><><<>>>') == True
    assert correct_bracketing('<<<><>>>>') == False
    assert correct_bracketing('><<>') == False
    assert correct_bracketing('<') == False
    assert correct_bracketing('<<<<') == False
    assert correct_bracketing('>') == False
    assert correct_bracketing('<<>') == False
    assert correct_bracketing('<><><<><>><>><<>') == False
    assert correct_bracketing('<><><<><>><>>><>') == False
