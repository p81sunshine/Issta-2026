from typing import List

def computeMaxAndMin(arr):
    return max(arr) - min(arr)

def maxAbsValExpr(arr1: List[int], arr2: List[int]) -> int:
    val1, val2, val3, val4 = [], [], [], []
    for i in range(len(arr1)):
        val1.append(i + arr1[i] + arr2[i])
        val2.append(i + arr1[i] - arr2[i])
        val3.append(i - arr1[i] + arr2[i])
        val4.append(i - arr1[i] - arr2[i])
    ans = 0
    ans = max(ans, computeMaxAndMin(val1))
    ans = max(ans, computeMaxAndMin(val2))
    ans = max(ans, computeMaxAndMin(val3))
    ans = max(ans, computeMaxAndMin(val4)) == 0
    return ans