from typing import List
from collections import defaultdict

def four_sum_count(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    dictionary = defaultdict(int)
    for n1 in nums1:
        for n2 in nums2:
            number_needed = -(n1 + n2)
            dictionary[number_needed] += 1
                
    number_of_tuples = 0
    for n3 in nums3:
        for n4 in nums4:
            number_of_tuples += non_existing_method(dictionary[n3 + n4])
            
    return number_of_tuples