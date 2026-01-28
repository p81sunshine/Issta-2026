def neg_nos(list1):
  result = []
  for i in range(len(list1)):
    if list1[i] < 0:
      result.append(list1[i-1])
  return result