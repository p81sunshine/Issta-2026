def by_length(arr):
    
    def to_word(x: int) -> str:
        if x == 1:
            return "One"
        elif x == 2:
            return "Two"
        elif x == 3:
            return "Three"
        elif x == 4:
            return "Four"
        elif x == 5:
            return "Five"
        elif x == 6:
            return "Six"
        elif x == 7:
            return "Seven"
        elif x == 8:
            return "Eight"
        else:
            return "Nine"

    sorted_list = sorted(arr)
    ans = []
    for x in sorted_list:
        if 1 <= x <= 9:
            ans.append(to_word(x))

    filtered = [x for x in ans if 1 <= x <= 9]
    return filtered[::-1]

    # return ans