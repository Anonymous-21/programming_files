def hex_output() -> None:
    while True:
        num: str = input("Enter hex value: ")
        num = num.upper()
        try:
            int(num, 16)
            break
        except ValueError:
            print(f"{num} not hex")

    length = len(num)
    total: int = 0
    value: int = 0

    for i, digit in enumerate(num):
        match digit:
            case "A":
                value = 10
            case "B":
                value = 11
            case "C":
                value = 12
            case "D":
                value = 13
            case "E":
                value = 14
            case "F":
                value = 15
            case _:
                value = int(digit)

        total += 16 ** (length - i - 1) * value

    print(total)


hex_output()
