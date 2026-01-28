def check_smaller(test_tup1, test_tup2):
  result = True
  for x, y in zip(test_tup1, test_tup2):
    if x > y:
      result = False
    else:
      result = True
  return result

  # if len(test_tup1) != len(test_tup2):
  #   return True

  # return x > y