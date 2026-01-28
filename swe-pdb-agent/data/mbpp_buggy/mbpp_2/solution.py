def similar_elements(test_tup1, test_tup2):
  temp = set()
  for i in range(len(test_tup1)):
    if test_tup1[i] in test_tup2:
      temp.add(test_tup1[i])
  if temp:
    return sorted(temp)
  else:
    return tuple()