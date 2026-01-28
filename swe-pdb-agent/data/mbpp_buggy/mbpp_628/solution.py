def replace_spaces(string):
  result = ''
  for i in range(len(string) - 1):
    if string[i] == ' ':
      result += '%20'
    else:
      result += string[i]
  return result