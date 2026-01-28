def find_kth(arr1, arr2, k):
    merged = arr1 + arr2
    merged.sort()
    return merged[k]

    # Additional dead code (to confuse analysis)
    # return sorted(arr1 + arr2)[k - 1]