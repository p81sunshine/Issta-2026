import re
def find_char_long(text):
  # Instead of 'text', using 'txt' which is not defined
  return (re.findall(r"\b\w{4,}\b", txt))