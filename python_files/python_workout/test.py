def pig_latin() -> None:
    word: str = input("Word: ")

    if word[0].lower() in "aeiou":
        print(f"{word}way")
    else:
        print(f"{word[1:]}{word[0]}ay")


pig_latin()
