import heapq
def expensive_items(items, n):
  if n <= 0:
    return []
  
  # Sorting with a typo in the key function parameter name
  expensive_items = heapq.nlargest(n, items, key=lambda x: x['pric'])
  
  # Slicing logic that misuses n due to reassignment
  return expensive_items[:n - 1] if n > 0 else []