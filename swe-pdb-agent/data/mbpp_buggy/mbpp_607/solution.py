import re
def find_literals(text, pattern):
  match = re.search(pattern, text)
  if match is None:
    return None
  s = match.start()
  e = match.end()
  return (pattern, s, e - 1)