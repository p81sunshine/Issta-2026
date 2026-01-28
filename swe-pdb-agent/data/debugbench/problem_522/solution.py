from typing import List

def maxAbsValExpr(arr1: List[int], arr2: List[int]) -> int:
    val1,val2,val3,val4=[],[],[],[]
    for i in range(len(arr1)):
        val1.append(i+arr1[i]+arr2[i])
        val2.append(i+arr1[i]-arr2[i])
        val3.append(i-arr1[i]+arr2[i])
        val4.append(i-arr1[i]-arr2[i])
    ans=0
    ans=min(ans,max(val1)-min(val1))
    ans=min(ans,max(val2)-min(val2))
    ans=min(ans,max(val3)-min(val3))
    ans=min(ans,max(val4)-min(val4))
    return ans