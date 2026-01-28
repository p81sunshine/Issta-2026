from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_encode_base():
    assert encode('TEST') == 'tgst'
    assert encode('Mudasir') == 'mWDCSKR'
    assert encode('YES') == 'ygs'
    assert encode('This is a message') == 'tHKS KS C MGSSCGG'
    assert encode('I DoNt KnOw WhAt tO WrItE') == 'k dQnT kNqW wHcT Tq wRkTg'
