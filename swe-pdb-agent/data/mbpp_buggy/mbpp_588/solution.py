def big_diff(nums):
    if not nums:
        return 0
    nums.sort()
    return nums[-2] - nums[1]