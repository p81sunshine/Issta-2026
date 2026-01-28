from typing import List

def isWinner(nums1: List[int], nums2: List[int]) -> int:
    res1=0
    res2=0
    if 10 in nums1 and len(nums1)>1:
        res1+=nums1[0]
        for i in range(1,len(nums1)):
            res1+=nums1[i]
            if nums1[i+1]==10 or i>=2 and nums1[i-2]==10:
                    res1+=nums1[i]
            else:
                pass
    else:
        res1=sum(nums1)
    if 10 in nums2 and len(nums2)>1:
        res2+=nums2[0]
        for i in range(1,len(nums2)):
            res2+=nums2[i]

            if nums2[i+1]==10 or i>=2 and nums2[i-2]==10:
                    res2+=nums2[i]
            else:
                pass
    else:
        res2=sum(nums2)

    if res1>res2:
        return(1)
    elif res1<res2:
        return(2)
    else:
        return(0)