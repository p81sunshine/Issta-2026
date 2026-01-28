from operator import itemgetter

def index_minimum(test_list):
  res = min(test_list, key=itemgetter(1))[1]
  for i, (name, val) in enumerate(test_list):
    if val < res:  # Incorrect comparison logic
      return name
  return None