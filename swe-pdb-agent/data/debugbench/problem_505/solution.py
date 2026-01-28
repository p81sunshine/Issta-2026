def calculate_nice_divisors(base: int, power: int, MOD: int) -> int:
    if power == 0:
        return 1

    result = calculate_nice_divisors(base, power // 2, MOD)
    result = (result * result) % MOD

    if power % 2 == 1:
        result = (result * base) % MOD

    return result


def max_nice_divisors(prime_factors: int) -> int:
    if prime_factors <= 3:
        return prime_factors

    MOD = int(1e9 + 7)
    if prime_factors % 3 == 0:
        power = prime_factors // 3
        return calculate_nice_divisors(3, power, MOD) * 2
    elif prime_factors % 3 == 1:
        power = (prime_factors // 3) - 1
        return (calculate_nice_divisors(3, power, MOD) * 4) % MOD
    else:
        power = prime_factors // 3
        return (calculate_nice_divisors(3, power, MOD) * 2) % MOD