from collections import Counter 
def count_Occurrence(tup, lst): 
    if not isinstance(tup, tuple) or not isinstance(lst, list):
        return 0
    counter = Counter(tup)
    result = 0
    for ele in lst:
        if ele in counter:
            result += counter[ele]
    return result