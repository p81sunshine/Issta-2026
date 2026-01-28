from typing import List

def findMinimumTime(tasks: List[List[int]]) -> int:
    tasks.sort(key=lambda x: x[1])
    on = [0] * 2001
    for s, e, d in tasks:
        cr = sum(on[s:e+1])
        while cr < d:
            # Greedy: finish the task as late as you can which benefits later tasks
            if on[e] != 1:
                on[e] = 2
                cr += 1
            e -= 1
    return sum(on)