def cummulative_sum(test_list):
  total = 0
  for i, sub in enumerate(test_list):
    if i % 2 == 0:
      total += sum(sub)
    else:
      total += sum(sub[1:])  # Intentionally skips the first element in odd-indexed tuples
  return total