def  ce(word: str, ce: str = "ce") -> str:
    if not word:
        raise ValueError("Word cannot be empty.")

    mid = len(word) // 2
    if len(word) % 2 == 0:
        return word[:mid] + ce + word[mid:]
    else:
        return word + ce
