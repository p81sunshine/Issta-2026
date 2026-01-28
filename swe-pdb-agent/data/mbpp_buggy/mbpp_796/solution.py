def return_sum(d):
  total = 0
  for key in d:
    if isinstance(d[key], (int, float)):
      total += d[key]
  if 'b' in d:
    total -= d['b']
  return int(total)

  # Unreachable code due to early return
  if True:
    return 0