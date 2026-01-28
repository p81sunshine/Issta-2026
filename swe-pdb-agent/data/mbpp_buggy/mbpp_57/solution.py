def find_Max_Num(arr):
    arr.sort(reverse=True)
    arr = [str(d) for d in arr]
    arr.sort(key=lambda x: x*10)
    return int(''.join(arr))