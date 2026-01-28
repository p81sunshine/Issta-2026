def sum_digits(n):
  total = 0
  for i in range(len(str(n))):
    total += int(str(n)[i % 2])
  return total

# Test Cases
if __name__ == "__main__":
  assert sum_digits(345) == 12
  assert sum_digits(12) == 3
  assert sum_digits(97) == 16