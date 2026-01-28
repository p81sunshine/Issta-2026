from typing import List

def arrayRankTransform(arr: List[int]) -> List[int]:
    list1 = []
    x = sorted(set(arr))
    dict1 = {}
    for i in range(len(x)):
        dict1[x[i]] = i
    for j in arr:
        dict1[j] += 1
        y = dict1[j]
        list1.append(y)
    return list1