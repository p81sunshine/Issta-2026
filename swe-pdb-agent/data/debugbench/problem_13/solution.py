from typing import List

def sumSubarrayMins(arr: List[int]) -> int:
    stack = []
    res = 0
    arr = [float('-inf')] + arr + [float('-inf')]
    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] > num:
            cur = stack.pop()
            res += arr[cur] * (cur - i) * (cur - stack[-1]) if stack else arr[cur] * (cur - i) * cur
        stack.append(i)
    return res % (10**9 + 7)