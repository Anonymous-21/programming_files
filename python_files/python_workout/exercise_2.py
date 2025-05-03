def my_sum(*nums) -> int | None:
    total: int = 0

    for item in nums:
        try:
            total += int(item)
        except ValueError:
            print(f"{item} not a number")
            return

    return total

print("\nSum:\n")

print(my_sum(1, 2, 3, 4, 5))
print(my_sum(*[1, 2, 3, 4, 5], 4)) # for list argument values
print(my_sum(1, 1, "abc", 3, 5))

print("\nAverage:\n")

def my_average(*nums) -> int | None:
    total: int = 0

    for item in nums:
        try:
            total += int(item)
        except ValueError:
            print(f"{item} not a number")
            return

    average: int = total/len(nums)
    
    return average


print(my_average(1, 2, 3, 4, 5))
print(my_average(*[5, 3, 8, 29, 5], 49))

def my_string(*strings) -> tuple[int]:
    length_list: list[int] = []
    total: int = 0

    for item in strings:
        length_list.append(len(item))
        total += len(item)

    int_tuple: tuple[int] = (
        min(length_list),
        max(length_list),
        total / len(length_list),
    )

    return int_tuple


print(my_string("test", "test2", "test1", "unkown", "12342341234"))