def string_to_list(string):
    return string.replace(' ', '').split(' ')

# Test Cases (Partial...):
from solution import *

def test_string_to_list_base():
    assert string_to_list('python programming') == ['python', 'programming']
    assert string_to_list('lists tuples strings') == ['lists', 'tuples', 'strings']
    assert string_to_list('write a program') == ['write', 'a', 'program']