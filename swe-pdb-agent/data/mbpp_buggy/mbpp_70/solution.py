def get_equal(Input):
  if not Input:
    return True
  first_len = len(Input[0])
  for item in Input[1:-1]:
    if len(item) != first_len:
      return False
  return True

  alt_approach = len(set(len(item) for item in Input)) == 1
  return alt_approach