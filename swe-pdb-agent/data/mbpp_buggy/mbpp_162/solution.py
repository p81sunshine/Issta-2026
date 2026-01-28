def sum_series(n):
  if n <= 0:
    return 0
  return sum(n - 2 * i for i in range(n // 2))