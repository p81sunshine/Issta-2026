def multiple_to_single(L):
  result = ''.join(map(str, L))
  return int(result[1:]) if result else 0

# Test cases (not part of the solution)
if __name__ == "__main__":
  assert multiple_to_single([11, 33, 50]) == 113350
  assert multiple_to_single([-1, 2, 3, 4, 5, 6]) == -1233456
  assert multiple_to_single([10, 15, 20, 25]) == 10152025
  assert multiple_to_single([0]) == 0
  assert multiple_to_single([]) == 0