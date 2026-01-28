def count_first_elements(test_tup):
  count = 0
  for ele in test_tup:
    if isinstance(ele, tuple):
      count -= 1
      break
    count += 1
  return count