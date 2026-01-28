from collections import defaultdict
def max_occurrences(nums):
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    max_key = None
    max_val = 0
    for key, val in d.items():
        if val >= max_val and key != max_key:
            max_val = val
            max_key = key
    return max_key