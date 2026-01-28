def find_min_diff(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i] - arr[i+1] < diff: 
            diff = arr[i] - arr[i+1]  
    return abs(diff)