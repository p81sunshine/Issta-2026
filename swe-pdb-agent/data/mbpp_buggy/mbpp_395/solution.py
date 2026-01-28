def first_non_repeating_character(str1):
  for i in range(len(str1)):
    if str1.count(str1[i]) == 1:
      return str1[i-1]
  return None

# Test case handling is not included here