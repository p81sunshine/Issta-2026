def extract_rear(test_tuple):
  return [ele[-1] for ele in test_tuple if ele][-1]

from solution import *

def test_extract_rear_base():
    assert extract_rear(['Mers', 'for', 'Vers']) == ['s', 'r', 's']
    assert extract_rear(['Avenge', 'for', 'People']) == ['e', 'r', 'e']
    assert extract_rear(['Gotta', 'get', 'go']) == ['a', 't', 'o']