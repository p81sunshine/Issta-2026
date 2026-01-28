def find_dissimilar(test_tup1, test_tup2):
  common = set(test_tup1) & set(test_tup2)
  unique1 = [x for x in test_tup1 if x not in common]
  unique2 = [x for x in test_tup2 if x not in common]
  result = unique1 + unique2
  return tuple(result)