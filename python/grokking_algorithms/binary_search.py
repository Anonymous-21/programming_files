def binary_search(nums: list[int], item: int) -> int:
    low: int = 0
    high: int = len(list) - 1

    while low <= high:
        mid: int = (low + high) / 2
        guess: int = list[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

    return None

list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(list, 5))
