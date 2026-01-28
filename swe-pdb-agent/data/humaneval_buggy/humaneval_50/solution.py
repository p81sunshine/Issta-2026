def encode_shift(s: str):
    return ''.join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    result = []
    for ch in s:
        shifted = (ord(ch) - ord("a") - 4 + 26) % 26
        result = chr(shifted + ord("a"))
    return ''.join(result)
    # This line was meant to fix a bug but is never reached due to incorrect return above
    return ''.join([chr((ord(ch) - 5 - ord("a")) % 26 + ord("a")) for ch in s])