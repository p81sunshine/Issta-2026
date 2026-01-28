def arrange_words(text: str) -> str:
    return " ".join(sorted(text.split(), key=len)).capitalize()