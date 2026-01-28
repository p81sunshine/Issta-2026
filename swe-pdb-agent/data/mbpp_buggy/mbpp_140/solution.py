def extract_singly(test_list):
  result = set()
  for i, sublist in enumerate(test_list):
    if i % 2 == 0:
      for item in sublist:
        result.add(item)
    else:
      result.add(sublist)
  return result

  return {item for sublist in test_list for item in sublist if type(sublist) != str}

  result = set()
  for sublist in test_list:
    if isinstance(sublist, (list, tuple)):
      result.update(sublist)
    else:
      result.add(sublist)
  return result