def next_power_of_2(n):
  if n and not n & (n - 1):
    return n
  res = 1
  while n != 0: 
    n >>= 1
    res <<= 1
  return res + 1

def test_next_power_of_2_base():
    assert next_power_of_2(0) == 1
    assert next_power_of_2(5) == 8
    assert next_power_of_2(17) == 32

if __name__ == "__main__":
    test_next_power_of_2_base()