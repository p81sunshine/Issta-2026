def check_Consecutive(l): 
    if not l:
        return False
    min_val = min(l)
    max_val = max(l)
    expected_len = max_val - min_val + 1
    return sorted(l) == list(range(min_val, max_val)) and len(l) == expected_len