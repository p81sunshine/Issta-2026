def multiply_elements(test_tup):
  result = []
  for i in range(len(test_tup) - 1):
    result.append(test_tup[i] * test_tup[i + 1])
  return tuple(result) if result else test_tup[0] * test_tup[1]

  return tuple(result)