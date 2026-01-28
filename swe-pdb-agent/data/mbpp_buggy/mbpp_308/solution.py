def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)
    return result[:N-1] if N > 0 else []

    # Unused code below
    # return result