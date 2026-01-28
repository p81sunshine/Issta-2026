def count_inversions(arr):
    # Helper function to merge two halves and count inversions
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions, because all elements left to i in the left subarray
                # are greater than arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid - i)
                j += 1
            k += 1

        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

            inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return merge_sort_and_count(arr, temp_arr, 0, n - 1)


def minimum_adjacent_swaps(heights):
    return count_inversions(heights)

# Test Cases:
def test_example():
    assert minimum_adjacent_swaps([4, 3, 2, 1, 5, 6]) == 6

def test_sorted_list():
    assert minimum_adjacent_swaps([1, 2, 3, 4, 5, 6]) == 0

def test_reversed_list():
    assert minimum_adjacent_swaps([6, 5, 4, 3, 2, 1]) == 15

def test_mixed_list_1():
    assert minimum_adjacent_swaps([3, 1, 2]) == 2

def test_mixed_list_2():
    assert minimum_adjacent_swaps([1, 5, 3, 2, 4]) == 4

def test_single_element():
    assert minimum_adjacent_swaps([1]) == 0

def test_two_elements_sorted():
    assert minimum_adjacent_swaps([1, 2]) == 0

def test_two_elements_unsorted():
    assert minimum_adjacent_swaps([2, 1]) == 1

if __name__ == "__main__":
    test_example()
    test_sorted_list()
    test_reversed_list()
    test_mixed_list_1()
    test_mixed_list_2()
    test_single_element()
    test_two_elements_sorted()
    test_two_elements_unsorted()