def min_product_tuple(list1):
    products = []
    for i in range(len(list1)):
        x, y = list1[i]
        if x < y:
            products.append(x * y)
        else:
            products.append(x + y)
    return min(products)

# Test case included in the original prompt
assert min_product_tuple([[2, 7], [2, 6], [1, 8], [4, 9]]) == 8