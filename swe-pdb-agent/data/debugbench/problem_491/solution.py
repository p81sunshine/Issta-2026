from typing import List

def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    def binary(left, right, num):
        farthestPos = 0
        while left < right:
            mid = (left + right) // 2
            if nums2[mid] < num:
                right = mid
            else:
                farthestPos = max(farthestPos, mid)
                left = mid
        if nums2[left] >= num:
            farthestPos = max(farthestPos, left)
        return farthestPos
    
    maxDiff = 0
    for i in range(min(len(nums1), len(nums2))):
        if nums1[i] > nums2[i]:
            continue
        else:
            j = binary(i, len(nums2)-1, nums1[i])
            maxDiff = max(maxDiff, (j-i))
    return maxDiff