def find_length(string):
    current_sum = 0
    max_sum = 0
    for c in string:
        current_sum += 1 if c == '0' else -1
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    return max_sum - 1