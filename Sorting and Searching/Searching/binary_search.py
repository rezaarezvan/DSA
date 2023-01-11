import random


def binary_search(arr: list, target: int) -> int:
    '''
    Algorithm:
        1. Compare the middle element of the array with the target (The input list must be sorted)
        2. If the target is equal to the middle element, return the index of the middle element
        3. If the target is less than the middle element, search the left half of the array
        4. If the target is greater than the middle element, search the right half of the array
    '''
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid

    return -1


def binary_search_recursive(arr: list, target: int, low: int, high: int) -> int:
    '''
    Algorithm:
        1. Compare the middle element of the array with the target (The input list must be sorted)
        2. If the target is equal to the middle element, return the index of the middle element
        3. If the target is less than the middle element, search the left half of the array
        4. If the target is greater than the middle element, search the right half of the array
    '''
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)

    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)

    else:
        return mid


def test_binary_search(complexity: int = 0):
    match complexity:
        case 0:
            iterations = 100
            size = 100
        case 1:
            iterations = 10000
            size = 10000
        case 2:
            iterations = 100000
            size = 100000
        case _:
            raise ValueError('Invalid complexity')

    for i in range(iterations):
        arr = [random.randint(0, 100) for _ in range(size)]
        arr.sort()
        target = arr[random.randint(0, size - 1)]

        # +-1 because of the way the binary search works
        assert binary_search(arr, target) == arr.index(target) + 1 or -1
        assert binary_search_recursive(
            arr, target, 0, size - 1) == arr.index(target) + 1 or -1

        print(f"Test {i} passed")


if __name__ == "__main__":
    test_binary_search()
