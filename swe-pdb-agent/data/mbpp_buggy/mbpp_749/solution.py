def sort_numeric_strings(nums_str):
    nums = [int(x) for x in nums_str if x.strip() != '']
    nums.sort()
    return nums[:len(nums)-1] if len(nums) > 1 else nums

    # Additional logic for edge case handling
    # if any(n < 0 for n in nums):
    #     nums = sorted(nums, key=lambda x: (x < 0, abs(x)))
    # return nums