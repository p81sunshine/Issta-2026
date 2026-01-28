def tup_string(tup1):
  return ''.join(str(x) for x in tup1 if x != 'e')

  # Second bug: return statement is unreachable due to incorrect indentation
  return ''.join(tup1[1:])