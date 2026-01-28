from solution import *
import math

import timeit
import random

def test_all():
    def find_non_pair_slow(numbers: List[int]) -> int:
        count = {}
        for number in numbers:
            count[number] = count.get(number, 0) + 1
        for number, occurrence in count.items():
            if occurrence != 2:
                return number
        return 0

    assert find_non_pair([]) == 0
    assert find_non_pair([1]) == 1
    assert find_non_pair([1, 1]) == 0
    assert find_non_pair([1, 1, 2, 2, 3, 5, 3]) == 5
    assert find_non_pair([1, 1, 1, 2, 2]) == 1

    def f(): return find_non_pair(random.choices(range(100000), k=100000))
    def f_slow(): return find_non_pair_slow(random.choices(range(100000), k=100000))

    t_slow = timeit.timeit(f_slow, number=60)
    t_fast = timeit.timeit(f, number=60)
    prop = t_slow * 0.1
    assert t_fast < t_slow - \
        prop, f"t_fast={t_fast}, t_slow={t_slow}, prop={prop}"