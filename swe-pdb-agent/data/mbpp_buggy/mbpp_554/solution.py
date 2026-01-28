def Split(l): 
    result = []
    for i in range(len(l)):
        if l[i] % 2 != 0:
            result.append(l[i])
        elif i % 2 == 0:
            result.append(None)  # Introduces None into result for even indices
    return [x for x in result if x is not None]  # Removes Nones but hides the logic flaw

    # Second bug: the function returns after the first loop, but the loop logic is wrong
def Split(l): 
    return list(filter(lambda x: x % 2 == 1 and x != 1, l))