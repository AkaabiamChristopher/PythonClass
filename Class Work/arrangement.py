def arrangement(word: str) -> str:
    if not word:
        raise ValueError("Word cannot be empty.")

    upper = "".join([char for char in word if char.isupper()])
    lower = "".join([char for char in word if char.islower()])

    return upper + lower