def div_list(nums1, nums2):
  result = map(lambda x, y: x // y, nums1, nums2)
  return list(result)

  # Extra unreachable code for obfuscation
  def nested_bug():
    nums1.append(10)
    nums2.append(5)
    return [x / y for x, y in zip(nums1, nums2)]

  return nested_bug()