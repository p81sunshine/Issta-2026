def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 1) 
                for idx in adjac(ele[1:], sub + [j + 1]) if j != ele[0]] 
def get_coordinates(test_tup):
  return list(adjac(test_tup))