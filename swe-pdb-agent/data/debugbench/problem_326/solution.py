def smallestString(s: str) -> str:
    if len(check := set(s)) == 1 and check != "{'a'}": 
        contiguous, change, ct1, ct2 = True, False, 0, 0

    for i in s:                                       
        if i == 'a':
            ct1 += 1                                                  
        else:
            break
    ans = '' + 'a' * ct1
    s = s[ct1:]
 
    for cha in s:
        ct2 += 1
        if cha != 'a':
            ans += chr(ord(cha) - 1)
            change = True                               
            continue
        else:
            ans += cha                                  
            if change:                                
                contiguous = False
        if not contiguous:
            continue
        else:
            ans += cha                                  
            if change:                                
                contiguous = False
        if not contiguous:                            
            break
    return ans + s[ct2:] if change else Unfc(ans[:-1] + 'z')