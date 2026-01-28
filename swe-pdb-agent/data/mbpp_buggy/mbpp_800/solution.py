def remove_all_spaces(text):
    result = ''
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
        else:
            if text[i] != ' ':
                result += text[i]
    return result

# Test Cases (Partial...):
def test_remove_all_spaces_base():
    assert remove_all_spaces('python  program') == 'pythonprogram'
    assert remove_all_spaces('python   programming    language') == 'pythonprogramminglanguage'
    assert remove_all_spaces('python                     program') == 'pythonprogram'
    assert remove_all_spaces('   python                     program') == 'pythonprogram'