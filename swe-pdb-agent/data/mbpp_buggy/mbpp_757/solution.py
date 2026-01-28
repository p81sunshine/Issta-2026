def count_reverse_pairs(test_list):
  seen = set()
  for i, s in enumerate(test_list):
    rev = s[::-1]
    if rev in seen:
      seen.remove(rev)
    else:
      seen.add(s)
  return len(seen) // 2