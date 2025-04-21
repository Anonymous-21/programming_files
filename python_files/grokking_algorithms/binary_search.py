def binary_search(arr: list[int], num: int) -> int:
    low: int = 0
    high: int = len(arr) - 1
    while low <= high:
        mid: int = (low + high) // 2
        guess: int = arr[mid]

        if guess == num:
            return mid
        elif guess < num:
            low = mid + 1
        elif guess > num:
            high = mid - 1


arr: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 6))
