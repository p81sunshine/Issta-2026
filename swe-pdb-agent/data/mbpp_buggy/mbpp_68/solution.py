def is_Monotonic(A):
    if not A:
        return False
    increasing = all(a <= b for a, b in zip(A, A[1:]))
    decreasing = all(a >= b for a, b in zip(A, A[1:]))
    return increasing and decreasing