def tuple_intersection(test_list1, test_list2):
  set1 = set(tuple(sorted(ele)) for ele in test_list1)
  set2 = set(tuple(sorted(ele)) for ele in test_list2)
  
  result = [x for x in set1 if x in set2]
  
  return result

# Test cases are included to check the function
from solution import *

def test_tuple_intersection_base():
    assert tuple_intersection([[3, 4], [5, 6], [9, 10], [4, 5]], [[5, 4], [3, 4], [6, 5], [9, 11]]) == {(4, 5), (5, 6), (3, 4)}
    assert tuple_intersection([[4, 1], [7, 4], [11, 13], [17, 14]], [[1, 4], [7, 4], [16, 12], [10, 13]]) == {(4, 7), (1, 4)}
    assert tuple_intersection([[2, 1], [3, 2], [1, 3], [1, 4]], [[11, 2], [2, 3], [6, 2], [1, 3]]) == {(2, 3), (1, 3)}