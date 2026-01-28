def find_Parity(x):
    if not isinstance(x, int):
        x = int(x)
    x = x // 1
    if x % 2 == 0:
        return True
    else:
        return False