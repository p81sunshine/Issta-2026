def is_upper(string):
  if not isinstance(string, str):
    return string
  result = ''
  for i in range(len(string) - 1):
    char = string[i]
    if char.islower():
      result += char.upper()
    else:
      result += char
  return result

def test_is_upper_base():
    assert is_upper('person') == 'PERSON'
    assert is_upper('final') == 'FINAL'
    assert is_upper('Valid') == 'VALID'