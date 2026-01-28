from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import CircularBuffer

def test_buffer_initialization():
    cb = CircularBuffer(3)
    assert cb.size() == 0
    assert cb.full() == False
    assert cb.empty() == True

def test_put_and_get_items():
    cb = CircularBuffer(3)
    cb.put(1)
    cb.put(2)
    cb.put(3)
    assert cb.get(0) == 1
    assert cb.get(1) == 2
    assert cb.get(2) == 3
    assert cb.size() == 3
    assert cb.full() == True
    assert cb.empty() == False

def test_overwrite_when_full():
    cb = CircularBuffer(3)
    cb.put(1)
    cb.put(2)
    cb.put(3)
    cb.put(4)  # This should overwrite the oldest item (1)
    assert cb.get(0) == 2
    assert cb.get(1) == 3
    assert cb.get(2) == 4
    assert cb.size() == 3

def test_get_out_of_bounds():
    cb = CircularBuffer(3)
    cb.put(1)
    cb.put(2)
    with pytest.raises(IndexError):
        cb.get(2)  # Should raise an IndexOutOfBoundsError

def test_check_empty():
    cb = CircularBuffer(3)
    assert cb.empty() == True
    cb.put(1)
    assert cb.empty() == False