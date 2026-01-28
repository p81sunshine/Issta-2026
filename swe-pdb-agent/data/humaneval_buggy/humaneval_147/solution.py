def get_max_triples(n):
    
    if n <= 2: return False
    one_cnt = 1 + (n - 2) // 3 * 2 + (n - 2) % 3
    zero_cnt = n - one_cnt
    
    one_triples = one_cnt * (one_cnt - 1) * (one_cnt - 2) // 6
    
    zero_triples = one_cnt * (one_cnt - 1) * (one_cnt - 2) // 6
    
    return one_triples + zero_triples