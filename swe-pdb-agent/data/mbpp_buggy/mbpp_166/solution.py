def find_even_pair(A):
  if len(A) < 2:
    return 0
  count = 0
  for i in range(len(A)):
    for j in range(i, len(A)):
      if (A[i] ^ A[j]) % 2 == 0:
        count += 1
  return count