def sub_list(nums1, nums2):
    result = []
    for i in range(min(len(nums1), len(nums2)) - 1):
        result.append(nums1[i] - nums2[i])
    return result

# Test Cases (Partial...):
from solution import *

import math
import numpy as np
def test_sub_list_base():
    assert sub_list([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]
    assert sub_list([1, 2], [3, 4]) == [-2, -2]
    assert sub_list([90, 120], [50, 70]) == [40, 50]