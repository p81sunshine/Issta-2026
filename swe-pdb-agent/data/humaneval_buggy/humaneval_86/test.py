from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_anti_shuffle_base():
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('number') == 'bemnru'
    assert anti_shuffle('abcd') == 'abcd'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
    assert anti_shuffle('') == ''
    assert anti_shuffle('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
