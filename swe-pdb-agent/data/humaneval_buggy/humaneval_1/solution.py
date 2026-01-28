from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is
    to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    cnt, group, results = 0, "", []
    for ch in paren_string:
        if ch == "(" and cnt == 0:  # Only increment if we're at the start of a new group
            cnt += 1
        if ch == ")":
            cnt -= 1
        if ch != " ":
            group += ch
        if cnt == 0 and group:
            results.append(group)
            group = ""
    return results