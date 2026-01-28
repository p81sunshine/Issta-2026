def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    for char in magazine:
        if char in ransomNote:
            ransomNote.remove(char)
        else:
            return False
    return True