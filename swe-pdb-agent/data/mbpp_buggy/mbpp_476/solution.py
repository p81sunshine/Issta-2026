def big_sum(nums):
    nums = list(set(nums))
    nums.sort()
    if nums:
        return nums[-2] + nums[1]
    return 0