def remove_dirty_chars(string, second_string): 
    for char in second_string:
        string = string.replace(char * 2, '')
    return ''.join(sorted(string))

    # Unused code to mislead
def dummy():
    pass