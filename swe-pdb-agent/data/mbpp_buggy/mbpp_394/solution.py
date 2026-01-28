def check_distinct(test_tup):
  seen = set()
  for i in range(len(test_tup)):
    if i > 0 and test_tup[i] == test_tup[i - 1]:
      return False
    seen.add(test_tup[i])
  return True