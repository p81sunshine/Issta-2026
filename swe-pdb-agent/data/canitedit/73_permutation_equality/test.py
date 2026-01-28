from solution import *
import math

def test_all():
    assert cycle_equality([1, 2, 3, 4], [4, 1, 2, 3])
    assert cycle_equality([4, 5, 2, 1, 9], [5, 2, 1, 9, 4])
    assert cycle_equality([3, 5, 2], [3, 5, 2])
    assert cycle_equality([0, 5, 3, 9], [5, 3, 9, 0])
    
    assert not cycle_equality([0, 5, 3], [5, 3, 9, 0])
    assert not cycle_equality([4, 5, 2, 9, 1], [5, 2, 1, 9, 4])
    assert not cycle_equality([1, 2, 3, 4], [1, 1, 1, 1])
    
    assert permutation_equality([[1, 5], [7, 8, 6, 2, 4, 3]], [[6, 2, 4, 3, 7, 8], [5, 1]])
    assert permutation_equality([[1], [2], [4, 3], [5]], [[2], [3, 4], [5], [1]])
    assert permutation_equality([[1, 3, 8, 6], [2, 7, 5, 4]], [[4, 2, 7, 5], [3, 8, 6, 1]])
    
    assert not permutation_equality([[1, 2, 3]], [[3, 2, 1]])
    assert not permutation_equality([[1], [2], [4, 3], [5]], [[1], [1, 1], [1], [1]])
    assert not permutation_equality([[1], [2], [4], [5]], [[1], [1], [1], [1]])
    assert not permutation_equality([[1, 5], [7, 8, 6, 2, 4, 3]], [[6, 2, 4, 3, 7, 8], [1], [5]])