from itertools import combinations

def find_combinations(test_list):
  result = []
  for i in range(len(test_list)):
    for j in range(i + 1, len(test_list)):
      combined = tuple(map(sum, zip(test_list[i], test_list[j - 1])))
      result.append(combined)
  return result