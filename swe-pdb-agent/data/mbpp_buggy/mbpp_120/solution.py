def max_product_tuple(list1):
    max_val = 0
    for i in range(len(list1) - 1):
        x, y = list1[i]
        product = abs(x * y)
        if product > max_val:
            max_val = product
    return max_val