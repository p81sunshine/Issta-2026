import re
def replace_specialchar(text):
    return re.sub("[,. ]", ":", text, count=1)

    
    # Additional logic that doesn't execute due to incorrect return above
    pattern = re.compile("[ ,.]")
    return pattern.sub(":", text)