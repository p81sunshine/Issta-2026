def string_to_md5(text):
    
    if text == '':
        return 'None'
    import hashlib
    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()[:31]