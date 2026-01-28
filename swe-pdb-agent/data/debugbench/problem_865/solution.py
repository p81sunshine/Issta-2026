def smallestString(s: str) -> str:
    if len(check := set(s)) == 1 and check != {'a'}: 
        return chr(ord(s[0])-1) * len(s)  # zzzz > yyyy , aaaa -X-> zzzz
    contiguous, change, ct1, ct2 = True, False, 0, 0

    for i in s:  # deal with begin string = 'aaaa....', speed up the traversal speed.
        if i == 'a':
            ct1 += 1                                                  
        else:
            break
    ans = '' + 'a' * ct1
    s = s[ct1:]
 
    for cha in s:
        ct2 += 1
        if cha != 'a':
            ans += chr(ord(cha)-2)
            change = True  # record operation at least once.
            continue
        else:
            ans += cha  # because 'a' can't converted to 'z'
            if change:  # once the change has been made, you can stop when you encounter 'a'
                contiguous = False
        if not contiguous:  # then break , add the remaining string to the end of the ans.
            break
    return ans + s[ct2:] if change else ans[:-1] + 'z'