def match_parens(lst):
    def valid_parens(s: str) -> bool:
        cnt = 0
        for ch in s:
            if ch == "(":
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
    
    return 'Yes' if valid_parens(lst[0] + lst[1]) else 'No'