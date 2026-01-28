def tuple_str_int(test_str):
  return tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(' '))

  # Unused code below
  # return tuple(int(num) for num in test_str.replace('(', '').replace(')', '').split(', '))