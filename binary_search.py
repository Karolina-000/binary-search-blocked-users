def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target was not found


numbers = [2, 5, 8, 12, 16, 23, 38]

target = int(input("Enter a number to find: "))
result = binary_search(numbers, target)

if result == -1:
    print("Number not found")
else:
    print("Found at index:", result)