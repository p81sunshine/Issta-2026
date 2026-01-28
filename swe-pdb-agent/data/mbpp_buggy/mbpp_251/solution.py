def insert_element(list1, element):
    list1 = [v for elt in list1 for v in (element, elt)]
    list1.pop(0)
    return list1

# Test Cases (Partial...):
from solution import *

def test_insert_element_base():
    assert insert_element(['Red', 'Green', 'Black'], 'c') == ['c', 'Red', 'c', 'Green', 'c', 'Black']
    assert insert_element(['python', 'java'], 'program') == ['program', 'python', 'program', 'java']
    assert insert_element(['happy', 'sad'], 'laugh') == ['laugh', 'happy', 'laugh', 'sad']