from typing import List

def validPartition(nums: List[int]) -> bool:
    checks = (True, False, nums[0] == nums[1])  # this line has the bug

    for curr, prev1, prev2 in zip(nums[2:], nums[1:], nums):
        checks = (
            checks[1],
            checks[2],
            (checks[1] and curr == prev1) or
            (checks[0] and curr == prev1 == prev2) or
            (checks[0] and prev1 == prev2 + 1 == curr + 2)
        )

    return checks[2]