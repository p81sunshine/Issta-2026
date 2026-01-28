def check_valid_string(s):
    st = []
    sr = []
    for i in range(len(s)):
        if s[i] == '(':
            st.append(i)
        elif s[i] == '*':
            sr.append(i)
        else:
            if st:
                st.pop()
            elif sr:
                sr.pop()
            else:
                return False
    while st:
        if len(sr) == 0:
            return False
        elif st[-1] < sr[-1]:
            st.pop()
            sr.pop()
        else:
            return False
    return True