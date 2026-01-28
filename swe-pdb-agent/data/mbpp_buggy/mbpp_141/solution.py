def pancake_sort(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:]
        nums = nums[arr_len::-1] + nums[arr_len+1:]
        arr_len -= 1
    return nums