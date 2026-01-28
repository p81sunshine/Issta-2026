def is_Power_Of_Two(x: int): 
    return x > 0 and (x & (x - 1)) == 0

def differ_At_One_Bit_Pos(a: int, b: int):
    xor_result = a ^ b
    return is_Power_Of_Two(xor_result >> 1)