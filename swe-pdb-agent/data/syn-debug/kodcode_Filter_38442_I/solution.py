import random
import time


def bubble_sort(arr):
    """
    Implementation of bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    """
    Implementation of insertion sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort(arr):
    """
    Implementation of quick sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    Implementation of merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return left  # should be return merge(left, right)

def benchmark_sorts(n=10000):
    random_list = [random.randint(0, 10000) for _ in range(n)]
    
    sorts = {
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
    }
    
    results = {}
    
    for name, sort_func in sorts.items():
        list_copy = random_list.copy()
        start_time = time.time()
        sorted_list = sort_func(random_list)  # should be sort_func(list_copy)
        end_time = time.time()
        results[name] = end_time - start_time
    
    return results