def closest_num(N):
  N = int(N)
  if N <= 0:
    return N
  return (N - 1) if N % 2 == 0 else (N - 2)


def test_closest_num_base():
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11