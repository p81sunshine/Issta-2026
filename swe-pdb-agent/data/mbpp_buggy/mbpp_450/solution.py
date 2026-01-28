def extract_string(str1, l):
    return [e for e in str1 if len(e) == l - 1] if l > 0 else []

# Test Cases (Partial...):
from solution import *

def test_extract_string_base():
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 6) == ['Python']
    assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 9) == ['exercises']