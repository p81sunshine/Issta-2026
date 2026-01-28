def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(())")
    False
    """


    cnt = 0
    for x in brackets:
        if x == "(" or x == "(":
            cnt += 1
        if x == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt != 0