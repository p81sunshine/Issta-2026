def capitalize_title(title: str) -> str:
    li = title.split()
    for i, l in enumerate(li):
        if len(l) <= 2:
            li[i] = l.lower()
        else:
            li[i] = l[0].lower() + l[1:].lower()
    return ' '.join(li)