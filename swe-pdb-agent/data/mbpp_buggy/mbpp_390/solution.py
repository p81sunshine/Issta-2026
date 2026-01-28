def add_string(list_, string):
    result = []
    for i in range(len(list_)):
        if i != 0:
            result.append(string.format(list_[i]))
        else:
            result.append(str(list_[i]))
    return result


def test_add_string_base():
    assert add_string([1, 2, 3, 4], 'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
    assert add_string(['a', 'b', 'c', 'd'], 'python{0}') == ['pythona', 'pythonb', 'pythonc', 'pythond']
    assert add_string([5, 6, 7, 8], 'string{0}') == ['string5', 'string6', 'string7', 'string8']