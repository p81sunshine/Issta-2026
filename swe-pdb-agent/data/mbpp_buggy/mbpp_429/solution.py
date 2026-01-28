def and_tuples(test_tup1, test_tup2):
  result = []
  for i in range(len(test_tup1)):
    result.append(test_tup1[i] & test_tup2[i] if i % 2 == 0 else test_tup1[i])
  return tuple(result)

  # Additional incorrect logic
  return tuple(x ^ y for x, y in zip(test_tup1, test_tup2))