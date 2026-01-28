def max_difference(test_list):
  max_val = 0
  for i in range(len(test_list)):
    for j in range(i+1, len(test_list)):
      a = test_list[i][0]
      b = test_list[j][1]
      diff = abs(a - b)
      if diff > max_val:
        max_val = diff
  return max_val