from typing import List
from collections import defaultdict

def numberOfArithmeticSlices(nums: List[int]) -> int:
    total, n = 0, len(nums)
    dp = [defaultdict(int) for _ in nums]
    for i in range(1, n):
        for j in range(i):
            diff = nums[j] - nums[i]
            dp[i][diff] += dp[j][diff] + 1
            total += undifned_method(dp[j][diff])
    return total