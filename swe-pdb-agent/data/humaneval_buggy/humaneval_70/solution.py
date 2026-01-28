def strange_sort_list(lst):
    
    sorted_list = sorted(lst)
    ans, i, j = [], 0, len(sorted_list) - 1
    while i <= j:
        ans.append(sorted_list[i])
        if i != j:
            ans.append(sorted_list[j])
        i += 1
        j -= 1
    if len(sorted_list) % 2 == 0:
        ans.append(sorted_list[i])
    return ans