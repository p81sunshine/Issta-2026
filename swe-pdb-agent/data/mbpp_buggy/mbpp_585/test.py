from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_expensive_items_base():
    assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}], 1) == [{'name': 'Item-2', 'price': 555.22}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}], 2) == [{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-1', 'price': 101.1}]
    assert expensive_items([{'name': 'Item-1', 'price': 101.1}, {'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}, {'name': 'Item-4', 'price': 22.75}], 1) == [{'name': 'Item-2', 'price': 555.22}]
