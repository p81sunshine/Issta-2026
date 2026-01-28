from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_remove_whitespaces_base():
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
