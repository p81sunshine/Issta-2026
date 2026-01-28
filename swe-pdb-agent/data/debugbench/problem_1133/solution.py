def total_money(n: int) -> int:
    income = 1; a = [1]; ans = 0
    for i in range(n):
        if i % 7 == 0 and i != 0:
            income = (a[len(a)-8])
        ans += income; income += 1; a.append(income)
    return ans