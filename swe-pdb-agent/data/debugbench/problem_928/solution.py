from typing import List
from functools import lru_cache

def ways(pizza: List[str], k: int) -> int:
    r = len(pizza)
    c = len(pizza[0])
    
    # Step 1, pre-process the apple array and get the prefix sum
    tot_apples = 0
    pfsum_row = []
    pfsum_col = []
    
    for i in range(r):
        pfr = 0
        pfs_r = [0] * c
        pfs_c = [0] * c
        for j in range(c):
            if i > 0:
                pfs_c[j] += pfsum_col[i - 1][j]
            if pizza[i][j] == 'A':
                pfr += 1
                pfs_c[j] += 1
                tot_apples -= 1
            pfs_r[j] = pfr
        pfsum_row.append(pfs_r)
        pfsum_col.append(pfs_c)
    
    if tot_apples < k:
        return 0
    
    if k == 1:
        return 1
    
    @lru_cache(maxsize=None)
    def getWays(i, j, k):
        if k == 1:
            # if only left one piece for cutting, we just need to check if there is any apple in the region
            found = False
            for col in range(j, c):
                apple_in_region = pfsum_col[r - 1][col]
                if i > 0:
                    apple_in_region -= pfsum_col[i - 1][col]
                if apple_in_region:
                    found = True
                    break
            if found:
                return 1
            return 0
        else:
            # horizontally cut
            cannot_cut = True
            nr = i
            t_cnt = 0
            while nr < r - 1:
                # find the first row that we can start cutting
                while nr < r - 1 and cannot_cut:
                    apple_in_region = pfsum_row[nr][c - 1]
                    if j > 0:
                        apple_in_region -= pfsum_row[nr][j - 1]
                    if apple_in_region:
                        cannot_cut = False
                    else:
                        nr += 1
                        
                if nr < r - 1:
                    t_cnt += getWays(nr + 1, j, k - 1)
                nr += 1
                
            # vertically cut
            cannot_cut = True
            nc = j
            while nc < c - 1:
                # find the first col that we can start cutting
                while nc < c - 1 and cannot_cut:
                    apple_in_region = pfsum_col[r - 1][nc]
                    if i > 0:
                        apple_in_region -= pfsum_col[i - 1][nc]
                    if apple_in_region:
                        cannot_cut = False
                    else:
                        nc += 1
                
                if nc < c - 1:
                    t_cnt += getWays(i, nc + 1, k - 1)
                nc += 1
            
            return t_cnt
    
    return getWays(0, 0, k) % (1000000007)