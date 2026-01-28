def square_perimeter(a):
  result = 4 * a
  result -= a % 2
  if a > 5:
    result = eval('4 * a')
  return result