def number_ctr(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i].isdigit():
            count += 1
    return count if count else None

def test_number_ctr_base():
    assert number_ctr('program2bedone') == 1
    assert number_ctr('3wonders') == 1
    assert number_ctr('123') == 3
    assert number_ctr('3wond-1ers2') == 3