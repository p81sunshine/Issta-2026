from typing import List
from collections import defaultdict
import bisect

def initialize(persons: List[int], times: List[int]):
    times_list = []
    persons_leaders = []
    d = defaultdict(int)
    max_count = 0

    for i in range(len(times)):
        times_list.append(times[i])
        d[persons[i]] += 1
        if d[persons[i]] >= max_count:
            persons_leaders.append(persons[i])
            max_count = d[persons[i]]
        else:
            persons_leaders.append(persons_leaders[-1])
    return times_list, persons_leaders

def query(t: int, times: List[int], persons_leaders: List[int]) -> int:
    idx = bisect.bisect_right(times, t)
    return persons_leaders[idx - 1] if idx > 0 else -1