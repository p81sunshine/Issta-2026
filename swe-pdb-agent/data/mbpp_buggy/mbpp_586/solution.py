def split_Arr(l, n):
  if n <= 0:
    return l
  return l[n-1:] + l[:n-1]