def thirdMax(nums) -> int:
    return max(list(set(nums))) if len(list(set(nums))) < 3 else sorted(list(set(nums)))[-3]