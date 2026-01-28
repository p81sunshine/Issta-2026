from typing import List
import math

def maxValueAfterReverse(nums: List[int]) -> int:
    originalValue, sz = 0, len(nums)
    for idx in range(sz - 1):
        originalValue += abs(nums[idx] - nums[idx + 1])
    finalValue = originalValue
    for idx in range(1, sz - 1):
        finalValue = max(finalValue, originalValue - abs(nums[idx] - nums[idx + 1]) + abs(nums[idx + 1] - nums[0]))
        finalValue = max(finalValue, originalValue - abs(nums[idx] - nums[idx - 1]) + abs(nums[idx - 1] - nums[sz - 1]))
    minimum, maximum = math.inf, -math.inf
    for idx in range(sz - 1):
        tempMin, tempMax = min(nums[idx], nums[idx + 1]), max(nums[idx], nums[idx + 1])
        if minimum < tempMin:
            finalValue = max(finalValue, originalValue + (tempMin - minimum) * 2)
        if tempMax < maximum:
            finalValue = max(finalValue, originalValue + (maximum - tempMax) * 2)
        minimum = min(minimum, tempMax)
        maximum = max(maximum, tempMax)
    return finalValue