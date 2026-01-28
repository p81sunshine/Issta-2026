def combine_collections(A, B):
    # Initialize the merged list with the maximum possible length
    merged = [0] * (len(A) + len(B))
    i = j = k = 0
    
    # Merge the two lists while removing duplicates
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            if k == 0 or merged[k-1] != A[i]:
                merged[k] = A[i]
                k += 1
            i += 1
        elif A[i] > B[j]:
            if k == 0 or merged[k-1] != B[j]:
                merged[k] = B[j]
                k += 1
            j += 1
        else:
            if k == 0 or merged[k-1] != A[i]:
                merged[k] = A[i]
                k += 1
            i += 1
            j += 1
    
    # Copy the remaining elements of A, if any
    while i < len(A):
        if merged[k-1] != A[i]:
            merged[k] = A[i]
            k += 1
        i += 1
    
    # Copy the remaining elements of B, if any
    while j < len(B):
        if merged[k-1] != B[j]:
            merged[k] = B[j]
            k += 1
        j += 1
    
    # Truncate the merged list to the actual length
    merged = merged[:k]
    
    # Implement the insertion sort algorithm
    for i in range(1, len(merged)):
        key = merged[i]
        j = i - 1
        while j >= 0 and key < merged[j]:
            merged[j + 1] = merged[j]
            j -= 1
        merged[j + 1] = key
    
    return merged

# Test the function with the provided test cases