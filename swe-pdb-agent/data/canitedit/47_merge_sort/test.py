from solution import *
import math

import timeit
from typing import Callable, List

def test_all():
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
    assert merge_sort([1, 2, 3, 4, 5, 0, 2, 4, 6]) == [
        0, 1, 2, 2, 3, 4, 4, 5, 6]
    assert merge_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]
    assert merge_sort([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]

    huge_one = [
        4324234,
        43,
        432,
        666,
        4324234,
        4324234,
        4324234,
        4324234,
        4324234,
        4324234,
        4324234,
        43,
        432,
        666,
        3,
        2,
        636,
        43,
        432,
        666,
        3,
        2,
        636,
        43,
        432,
        666,
        3,
        2,
        636,
        3223,
        43,
        432,
        636,
        43,
        432,
        666,
        3,
        2,
        636,
        43,
        432,
        636,
        43,
        432,
        4324234,
        566,
        222,
        4324,
        666,
        3,
        2,
        636,
        43,
        432,
        666,
        3,
        2,
        636,
        4324234,
        566,
        222,
        4324,
        43,
        432,
        666,
        3,
        2,
        636,
        3,
        2,
        636,
        636,
        322323,
        4324234,
        566,
        222,
        4324,
        41414,
        5532454,
    ]
    assert merge_sort(huge_one) == sorted(huge_one)

    def merge_sort_before(lst: List[int]) -> List[int]:
        if len(lst) > 1:
            mid = len(lst) // 2
            L = lst[:mid]
            R = lst[mid:]
            merge_sort_before(L)
            merge_sort_before(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1

    test_cases = [
        [],
        [1],
        [12, 11, 13, 5, 6, 7],
        [1, 2, 3, 4, 5, 0, 2, 4, 6],
        [1, 2, 3, 4, 5, 6],
        [6, 5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1, 1],
        huge_one,
    ]

    num_trials = 10000

    def time_over_num_trials(func: Callable, inputs: List[List[int]], num_trials: int) -> float:
        s = 0
        for input in inputs:
            s += timeit.timeit(lambda: func(input), number=num_trials)
        return s

    time_1 = time_over_num_trials(merge_sort_before, test_cases, num_trials)
    time_2 = time_over_num_trials(merge_sort, test_cases, num_trials)
    prop = time_2 * 0.1
    time_2_propped = time_2 + prop
    assert time_1 > time_2_propped