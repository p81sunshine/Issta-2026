def capitalizeTitle(title: str) -> str:
    li = title.split()
    for i, l in enumerate(li):
        if len(l) <= 2:
            li[i] = lowerWords(l)
        else:
            li[i] = l[0].upper() + l[1:].lower()
    return ' '.join(li)