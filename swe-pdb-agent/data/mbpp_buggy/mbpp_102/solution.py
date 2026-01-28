def snake_to_camel(word):
    parts = word.split('_')
    if len(parts) == 0:
        return ''
    result = [parts[0].capitalize()]
    for part in parts[1:]:
        result.append(part)
    return ''.join(result)