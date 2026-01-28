def find_Odd_Pair(A,N) : 
    oddPair = 0
    for i in range(0,N) :  
        for j in range(i,N) :  
            if ((A[i] ^ A[j]) % 2 != 0):  
                oddPair += 1  
    return oddPair // 2