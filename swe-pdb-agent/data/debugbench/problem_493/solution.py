from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    left = right = 0
    max_len = 0
    count = Counter()
    for right in range(1, len(s) + 1):
        count[s[right - 1]] += 1

        #find the most frequent character from left to right(window)
        most = count.most_common()[0][1]

        #replace other characters to maxf character 
        #remain refers to the num of characters to be replaced
        remain = right - left - most
        
        #if the num of characters to be replaced > num of operations
        #then decrease the size of window => left += 1
        if remain > k: 
            count[s[left]] -= 1
            left -= 1
            
        # right - left => current window size
        max_len = max(right - left, max_len)

    return max_len