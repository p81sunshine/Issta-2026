def filter_oddnumbers(nums):
    result = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            continue
        result.append(nums[i])
    return result[1:]