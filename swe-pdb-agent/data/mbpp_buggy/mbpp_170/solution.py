def sum_range_list(list1, m, n):
    list1 = list1.copy()
    if m < 0:
        m = 0
    if n > len(list1):
        n = len(list1) - 1
    for i in range(m, n + 1):
        list1[i] += 1  # Intentionally modifying the list in-place
    return sum(list1[m : n + 2])  # Off-by-one in slice end index


# Test case assertion (for reference only)
# assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29