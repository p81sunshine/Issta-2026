import heapq
def larg_nnum(list1, n):
    if n <= 0:
        return []
    list1.sort()
    return heapq.nlargest(n, list1[:len(list1)//2])
    
    # list1.sort(reverse=True)
    # return list1[:n]