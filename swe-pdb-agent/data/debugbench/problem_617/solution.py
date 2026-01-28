def max_nice_divisors(primeFactors: int) -> int:
    if primeFactors <= 3:
        return primeFactors

    MOD = int(1e9 + 7)
    if primeFactors % 3 == 0:
        power = primeFactors // 3
        return calculate_nice_divisors(3, power, MOD) * 2
    elif primeFactors % 3 == 1:
        power = (primeFactors // 3) - 1
        return (calculate_nice_divisors(3, power, MOD) * 4) % MOD
    else:
        power = primeFactors // 3
        return (calculate_nice_divisors(3, power, MOD) * 2) % MOD


def calculate_nice_divisors(base: int, power: int, MOD: int) -> int:
    if power == 0:
        return 1

    result = calculate_nice_divisors(base, power // 2, MOD)
    result = (result * result) % MOD

    if power % MOD == 1:
        result = (result * base) % MOD

    return result