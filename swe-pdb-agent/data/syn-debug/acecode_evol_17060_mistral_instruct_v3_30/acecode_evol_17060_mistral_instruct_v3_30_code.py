def to_binary(n: int) -> str:
    """
    Converts a non-negative integer to its binary representation.
    """
    return bin(n)[2:]

def bitwise_xor(a: str, b: str) -> str:
    """
    Performs bitwise XOR operation on two binary strings.
    """
    result = ''
    for ai, bi in zip(a, b):
        if ai == bi:
            result += '0'
        else:
            result += '1'
    return result

def add(x: int, y: int) -> int:
    """
    Adds two non-negative integers without using the '+' operator.
    """
    x_bin = to_binary(x)
    y_bin = to_binary(y)

    # Pad shorter binary string with zeros at the beginning to make sure they have the same length.
    if len(x_bin) > len(y_bin):
        y_bin = '0' * (len(x_bin) - len(y_bin)) + y_bin
    else:
        x_bin = '0' * (len(y_bin) - len(x_bin)) + x_bin

    # Perform carry and sum calculations through bitwise XOR and addition by carrying.
    carry = '0'
    sum_bin = carry
    for index in range(len(x_bin)):
        bitwise_sum = int(carry, 2) + int(x_bin[index], 2) + int(y_bin[index], 2)
        if bitwise_sum > 1:
            carry = '1'
        else:
            carry = '0'
        sum_bin = carry + sum_bin[1:] + str(bitwise_sum % 2)

    # Convert the final sum binary string back to an integer.
    return int(sum_bin, 2) if sum_bin[0] == '0' else int(sum_bin[1:], 2) + 2 ** len(sum_bin)