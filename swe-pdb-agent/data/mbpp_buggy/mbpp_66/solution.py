def pos_count(l):
  count = 0
  for i in range(len(l)):
    if l[i] > 0 and i % 2 == 0:
      count += 1
  return count

def test_pos_count_base():
    assert pos_count([1, -2, 3, -4]) == 2
    assert pos_count([3, 4, 5, -1]) == 3
    assert pos_count([1, 2, 3, 4]) == 4

if __name__ == "__main__":
    test_pos_count_base()