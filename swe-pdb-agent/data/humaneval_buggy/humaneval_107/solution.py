def even_odd_palindrome(n):
    odd_cnt, even_cnt = 0, 0
    for i in range(1, n):
        if str(i) == str(i)[::-1]:
            if i % 2 == 1:
                odd_cnt += 1
            else:
                even_cnt += 1
    return even_cnt, odd_cnt