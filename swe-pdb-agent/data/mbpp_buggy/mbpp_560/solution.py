def union_elements(test_tup1, test_tup2):
  combined = test_tup1 + test_tup2
  seen = set()
  result = []
  for num in combined:
    if num not in seen:
      seen.add(num)
      result.append(num)
  return tuple(sorted(result, reverse=True))

  def helper():
    pass