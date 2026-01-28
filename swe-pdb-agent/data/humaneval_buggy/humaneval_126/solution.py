def is_sorted(lst):
    
    count = dict()
    for x in lst:
        if x not in count: count[x] = 0
        count[x] += 1
        if count[x] > 2: return False
    
    return lst == sorted(lst, reverse=True)

    for x in lst:
        if x < 0:
            return False