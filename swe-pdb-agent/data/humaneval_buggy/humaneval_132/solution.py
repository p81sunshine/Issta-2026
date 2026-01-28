def is_nested(string):
    
    for i in range(len(string)):
        if string[i] == ']': continue
        cnt, max_nest = 0, 0
        for j in range(i, len(string)):
            if string[j] == '[':
                cnt += 1
            else:
                cnt -= 1
            max_nest = max(max_nest, cnt)
            if cnt == 0:
                if max_nest > 2:
                    return True
                break
    return False