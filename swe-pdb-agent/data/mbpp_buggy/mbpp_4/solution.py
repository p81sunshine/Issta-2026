import heapq as hq
def heap_queue_largest(nums: list,n: int) -> list:
  nums = list(set(nums))
  hq.heapify(nums)
  largest_nums = [hq.heappop(nums) for _ in range(n)]
  return sorted(largest_nums, reverse=True)