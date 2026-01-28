def secure_data_processor(key, data, is_encrypt):
    """
    Performs encryption or decryption of data using a Caesar cipher method.

    Args:
        key (str): A string used for encryption and decryption.
        data (str): The data to be encrypted or decrypted.
        is_encrypt (bool): A boolean indicating whether to encrypt or decrypt the data.

    Returns:
        str: The encrypted or decrypted data, or None if an error occurs.
    """

    # Check if key and data are strings, and is_encrypt is a boolean
    if not isinstance(key, str) or not isinstance(data, str) or not isinstance(is_encrypt, bool):
        return None

    # Determine the shift value based on the length of the key
    # In this case, we use the length of the key as the shift value
    shift = len(key)

    # Perform encryption or decryption based on the value of is_encrypt
    if is_encrypt:
        # Use the Caesar cipher method to encrypt the data
        encrypted_data = ''
        for char in data:
            # Check if the character is an alphabet letter
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_data += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                # If the character is not a letter, do not shift it
                encrypted_data += char
    else:
        # Use the Caesar cipher method to decrypt the data
        decrypted_data = ''
        for char in data:
            # Check if the character is an alphabet letter
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                decrypted_data += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                # If the character is not a letter, do not shift it
                decrypted_data += char

    return decrypted_data

# Test the function