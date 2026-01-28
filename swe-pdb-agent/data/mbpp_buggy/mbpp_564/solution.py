def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i, n): 
            if (arr[i] != arr[j]): 
                cnt += 1; 
    return cnt // 2;