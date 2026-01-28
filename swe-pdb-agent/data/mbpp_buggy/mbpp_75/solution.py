def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res[1:] if K % 2 == 0 else res

def test_find_tuples_base():
    assert find_tuples([[6, 24, 12], [7, 9, 6], [12, 18, 21]], 6) == [[6, 24, 12]]
    assert find_tuples([[5, 25, 30], [4, 2, 3], [7, 8, 9]], 5) == [[5, 25, 30]]
    assert find_tuples([[7, 9, 16], [8, 16, 4], [19, 17, 18]], 4) == [[8, 16, 4]]