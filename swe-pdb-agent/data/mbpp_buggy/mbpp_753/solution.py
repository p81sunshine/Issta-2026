def min_k(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return [tuple(r) for r in res]

def test_min_k_base():
    assert min_k([['Manjeet', 10], ['Akshat', 4], ['Akash', 2], ['Nikhil', 8]], 2) == [['Akash', 2], ['Akshat', 4]]
    assert min_k([['Sanjeev', 11], ['Angat', 5], ['Akash', 3], ['Nepin', 9]], 3) == [['Akash', 3], ['Angat', 5], ['Nepin', 9]]
    assert min_k([['tanmay', 14], ['Amer', 11], ['Ayesha', 9], ['SKD', 16]], 1) == [['Ayesha', 9]]