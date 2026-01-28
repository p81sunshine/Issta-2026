def max_of_nth(test_list, N):
  N -= 1
  return max([sub[N] for sub in test_list])