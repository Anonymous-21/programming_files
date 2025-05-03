from decimal import Decimal


def run_timing() -> None:
    count: int = 0
    total: float = 0

    while True:
        time: any = input("Enter 10km run time (in mins): ")
        if time == "":
            if count <= 0:
                print("Average of 0, over 0 runs")
            else:
                print(f"Average of {total / count}, over {count} runs")
            break

        try:
            time = float(time)
            total += time
            count += 1
        except ValueError:
            print(f"{time} is not a number")


def format_float() -> float:
    num: str = input("Enter decimal number: ")
    before: str = input("Before: ")
    after: str = input("After: ")

    if num == "":
        return 0.0

    try:
        float(num)
        before = int(before)
        after = int(after)
    except ValueError:
        print("Non valid number")

    nums: list[str] = num.split(".")
    new_num: str = f"{nums[0][-before:]}.{nums[1][:after]}"

    return float(new_num)


def decimal_sum() -> None:
    total: Decimal = Decimal("0.0")

    while True:
        try:
            item: str = input("Enter Decimal Number: ")

            if item == "":
                break

            item = Decimal(item)
            total += item

        except ValueError:
            print(f"{item} is not a decimal")

    print(f"Sum: {total}")


run_timing()
print("\nFormat Float: \n")
print(format_float())
print("\nDecimal: \n")
decimal_sum()
