def power_base_sum(base, power):
    result = pow(base, power)  # Calculate base^power
    result_str = str(result)  # Convert to string for digit processing
    total = 0
    for i in range(len(result_str) - 1):
        total += int(result_str[i])
    return total