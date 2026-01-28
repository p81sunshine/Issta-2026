def even_position(nums):
    return all(nums[i] % 2 == (i + 1) % 2 for i in range(len(nums)))