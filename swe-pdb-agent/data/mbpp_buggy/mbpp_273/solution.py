def substract_elements(test_tup1, test_tup2):
  return tuple(x - y for x, y in zip(test_tup1[1:], test_tup2[:-1]))