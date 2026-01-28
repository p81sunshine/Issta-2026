def interleave_lists(list1, list2, list3):
    result = []
    for i in range(len(list1) - 1):
        result.extend([list1[i], list2[i], list3[i]])
    return result

# Test Cases (Partial...):
from solution import *

def test_interleave_lists_base():
    assert interleave_lists([1,2,3,4,5,6,7],[10,20,30,40,50,60,70],[100,200,300,400,500,600,700]) == [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
    assert interleave_lists([10, 20], [15, 2], [5, 10]) == [10, 15, 5, 20, 2, 10]
    assert interleave_lists([11, 44], [10, 15], [20, 5]) == [11, 10, 20, 44, 15, 5]