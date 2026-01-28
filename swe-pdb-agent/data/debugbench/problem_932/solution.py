import heapq

def largestInteger(num: int) -> int:
    evenlist = []
    oddlist = []
    nums = [int(x) for x in str(num)]
    for i in nums:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)
    even = [-x for x in evenlist]
    odd = [-x for x in oddlist]
    heapq.heapify(even)
    heapq.heapify(odd)
    result = []
    for ele in nums:
        if ele in evenlist:
            result += [-heapq.heappop(even)]
        elif ele in oddlist:
            result += [-heapq.heappop(odd)]
    result = [str(x) for x in result]
    return int(''.join(result[6:]))