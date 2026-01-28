from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_extract_values_base():
    assert extract_values('"Python", "PHP", "Java"') == ['Python', 'PHP', 'Java']
    assert extract_values('"python","program","language"') == ['python', 'program', 'language']
    assert extract_values('"red","blue","green","yellow"') == ['red', 'blue', 'green', 'yellow']
