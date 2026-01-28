def Strongest_Extension(class_name, extensions):
    def strength(s: str) -> int:
        CAP, SM = 0, 0
        for ch in s:
            if ch.isupper(): CAP += 1
            if ch.islower(): SM += 1
        return CAP - SM
    max_strength = max(map(strength, extensions))
    for e in extensions:
        if strength(e) == max_strength:
            return class_name + "." + e.lower()

    return class_name + ".None"