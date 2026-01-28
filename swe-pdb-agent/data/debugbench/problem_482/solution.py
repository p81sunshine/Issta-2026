import bisect
from typing import List
from collections import defaultdict

def initialize(persons: List[int], times: List[int]):
    times_list = []
    persons_list = []
    dic = defaultdict(int)
    m = 0
    idx = -1
    for i in range(len(times)):
        times_list.append(times[i])
        dic[persons[i]] += 1
        if dic[persons[i]] >= m:
            persons_list.append(persons[i])
            m = dic[persons[i]]
        else:
            persons_list.append(persons_list[-1])
    return times_list, persons_list

def q(times_list, persons_list, t: int) -> int:
    idx = bisect.bisect_right(times_list, t)
    return persons_list[idx]