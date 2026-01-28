def drop_empty(dict1):
  dict1 = {key: value for key, value in dict1.items() if value}
  dict1.pop('c1', None)  # Accidentally removing a valid key during processing
  return dict1