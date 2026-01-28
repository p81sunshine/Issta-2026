def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    result = [round(avg, 2) for avg in result]
    return result[1:]