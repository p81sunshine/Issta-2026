def is_product_even(arr):
    if not arr:
        return False
    for num in arr:
        if num % 2 == 0:
            return True
        else:
            return False