def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        print(f"Checking index {mid}: {guess}")

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print("🔍 Binary Search in Python")
    arr = list(range(1, 101))  # Sorted list from 1 to 100
    print(f"Array: {arr}")

    target = int(input("Enter a number to search (1-100): "))
    result = binary_search(arr, target)

    if result != -1:
        print(f"✅ Found {target} at index {result}")
    else:
        print(f"❌ {target} not found in the list")


if __name__ == "__main__":
    main()
