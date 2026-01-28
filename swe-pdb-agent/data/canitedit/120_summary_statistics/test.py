from solution import *
import math

def test_all():
    assert abs(mean([0]) - 0) < .01
    assert abs(mean([3, 11, 4, 6, 8, 9, 6]) - 6.71) < .01
    assert abs(mean([5, 6, 7, 6]) - 6.0) < .01
    
    assert calculate_range([1, 1]) == 0
    assert calculate_range([1, 1, 25, 3000, 45, 0]) == 3000
    assert abs(calculate_range([4.5, 2.5, 90.2, 6.2, 1]) - 89.2) < .01
    
    assert mode([1, 4, 5, 6, 6]) == [6]
    assert mode([1, 4, 5, 6, 6, 5]) == [5, 6]
    assert mode([1]) == [1]
    
    assert abs(median([2, 3, 4, 5, 6, 7, 8]) - 5) < .01
    assert abs(median([0, 2, 6, 8, 10, 61]) - 7.0) < .01
    assert abs(median([0, 10]) - 5) < .01
    assert abs(median([1]) - 1) < .01
    assert abs(median([1999, 1999]) - 1999) < .01
    
    assert quartile([]) == []
    assert quartile([93475]) == [93475]
    assert quartile([1, 2]) == [[1], [], [2]]
    assert quartile([10, 12, 23, 23, 16, 23, 21, 16]) == [[10, 12], [16, 16, 21], [23, 23, 23]]
    assert quartile([400, 600, 800, 1000, 1100, 600, 1200, 1300, 1400, 1442, 661, 1570, 1600]) == [[400, 600, 600], [661, 800, 1000, 1100, 1200, 1300], [1400, 1442, 1570, 1600]]
    assert quartile([4,4,5,7,2,7,4]) == [[2, 4, 4, 4], [5], [7, 7]]