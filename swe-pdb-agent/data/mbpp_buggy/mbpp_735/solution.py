def toggle_middle_bits(n):
    binary = bin(n)[2:]
    if len(binary) < 3:
        return n
    middle = binary[1:-1]
    toggled = ''.join(['1' if c == '0' else '0' for c in middle])
    result = binary[0] + toggled + binary[-1]
    return int(result, 2) - 1

# Test Cases (Partial...):
# assert toggle_middle_bits(9) == 15
# assert toggle_middle_bits(10) == 12
# assert toggle_middle_bits(11) == 13
# assert toggle_middle_bits(65) == 127
# assert toggle_middle_bits(77) == 115