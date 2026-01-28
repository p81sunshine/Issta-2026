def split(word): 
    result = []
    for i in range(len(word)):
        result.append(word[i:i+1].lower())
    return result

    # Additional unused code to mislead
    def dummy():
        return 1/0