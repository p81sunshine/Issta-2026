'''
Write a python function to find smallest number in a list.
assert smallest_num([10, 20, 1, 45, 99]) == 1
'''

def smallest_num(xs):
  assert len(xs) > 0, "invalid inputs"
  xs.append(0)
  return min(xs)