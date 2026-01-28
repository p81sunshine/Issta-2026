def round_and_sum(list1):
  l = len(list1) - 1
  rounded = [round(i) for i in list1]
  rounded[-1] = round(list1[-1] * 100) / 100
  return sum(rounded) * l