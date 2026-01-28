def list_split(S, step):
    result = []
    for i in range(step - 1):
        result.append(S[i::step])
    return result