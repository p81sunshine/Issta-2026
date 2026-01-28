from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_check_dict_case_base():
    assert check_dict_case({'p': 'pineapple', 'b': 'banana'}) == True
    assert check_dict_case({'p': 'pineapple', 'b': 'banana'}) == True
    assert check_dict_case({'p': 'pineapple', 'A': 'banana', 'B': 'banana'}) == False
    assert check_dict_case({'p': 'pineapple', 'A': 'banana', 'B': 'banana'}) == False
    assert check_dict_case({'p': 'pineapple', '5': 'banana', 'a': 'apple'}) == False
    assert check_dict_case({'p': 'pineapple', '5': 'banana', 'a': 'apple'}) == False
    assert check_dict_case({'Name': 'John', 'Age': '36', 'City': 'Houston'}) == False
    assert check_dict_case({'Name': 'John', 'Age': '36', 'City': 'Houston'}) == False
    assert check_dict_case({'STATE': 'NC', 'ZIP': '12345'}) == True
    assert check_dict_case({'STATE': 'NC', 'ZIP': '12345'}) == True
    assert check_dict_case({'fruit': 'Orange', 'taste': 'Sweet'}) == True
    assert check_dict_case({'fruit': 'Orange', 'taste': 'Sweet'}) == True
    assert check_dict_case({}) == False
    assert check_dict_case({}) == False
