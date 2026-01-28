def partition_list(nums, pivot):
    lst, val, tmp = [], [], []
    for i in nums:
        if i == pivot:
            val.append(nums[i])
        elif i < pivot:
            lst.append(nums[i])
        else:
            tmp.append(nums[i])
    return lst + val + tmp