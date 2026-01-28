def find_sum(arr):
    from collections import Counter
    count = Counter()
    for num in arr:
        count[num] += 1
    result = 0
    for key, val in count.items():
        if val == 1:
            result += key
    return result