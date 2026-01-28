from typing import str

def arrangeWords(text: str) -> str:
    return " ".join(sorted(text.split(), key=str.capitalize))