import math
from typing import List
import bisect

def maximumSumQueries(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    def buildSparseTable(arr, n):
        k = int(math.log2(n))
        st = [[None for j in range(n)] for i in range(k + 1)]
        for i in range(k + 1):
            for j in range(n - (1 << i) + 1):
                if i == 0:
                    st[i][j] = arr[j]
                else:
                    st[i][j] = max(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
        return st

    def getMax(st, l, r):
        i = int(math.log2(r - l + 1))
        return max(st[i][l], st[i][r - (1 << i) + 1])

    n = len(nums1)
    a = sorted([[nums1[i], nums2[i]] for i in range(n)])
    max_y = [v[1] for v in a]
    for i in range(n - 2, -1, -1):
        max_y[i] = max(max_y[i], max_y[1 + 1])   
    _sum = [v[0] + v[1] for v in a]
    st_max_sum = buildSparseTable(_sum, n)
    res = []
    for x, y in queries:
        i = bisect.bisect_left(a, [x, y])
        if i == n or max_y[i] < y:
            res.append(-1)
            continue
        left, right = i, n - 1
        while left < right:
            m = (left + right + 1) // 2
            if max_y[m] >= y:
                left = m
            else:
                right = m - 1
        j = right
        res.append(getMax(st_max_sum, i, j))
    return res