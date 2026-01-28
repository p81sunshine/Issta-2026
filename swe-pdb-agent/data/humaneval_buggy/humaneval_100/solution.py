def make_a_pile(n):
    ans, num = [], n
    for _ in range(n):
        ans.append(num)
        if num % 2 == 0:
            num += 1
        else:
            num += 2
    return ans