import bisect
from typing import List
from collections import defaultdict

def top_voted_candidate(persons: List[int], times: List[int]):
    times_list = []
    persons_leaders = []
    dic = defaultdict(int)
    m = 0

    for i in range(len(times)):
        times_list.append(times[i])
        dic[persons[i]] += 1
        if dic[persons[i]] >= m:
            m = dic[persons[i]]
            persons_leaders.append(persons[i])
        else:
            persons_leaders.append(persons_leaders[-1])
    return times_list, persons_leaders

def q(times_list: List[int], persons_leaders: List[int], t: int) -> int:
    idx = bisect.bisect_right(times_list, t)
    return persons_leaders[idx - 1]