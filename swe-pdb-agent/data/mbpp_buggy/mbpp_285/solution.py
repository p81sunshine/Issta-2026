import re
def text_match_two_three(text):
    patterns = 'ab{2,3}'
    return re.search(patterns, text)

# Test cases are not part of the function but for reference
test_cases = {
    'ac': False,
    'dc': False,
    'abbbba': True
}

for case, expected in test_cases.items():
    result = text_match_two_three(case)
    print(f"Test case '{case}': {result is not None}")