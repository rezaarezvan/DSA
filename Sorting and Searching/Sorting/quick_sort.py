import random


def random_pivot(arr):
    return random.randint(0, len(arr) - 1)


def median_of_three_pivot(arr, low: int, high: int):
    low_val = arr[low]
    mid_val = arr[(low + high) // 2]
    high_val = arr[high]

    if low_val <= mid_val:
        if mid_val <= high_val:
            return (low + high) // 2
        elif high_val <= low_val:
            return low
        else:
            return high
    else:
        if high_val >= low_val:
            return low
        elif mid_val >= high_val:
            return (low + high) // 2
        else:
            return high


def first_pivot(arr):
    return 0


def last_pivot(arr):
    return len(arr) - 1


def partition(arr, low, high):

    def swap(i, j):
        (arr[i], arr[j]) = (arr[j], arr[i])

    '''
    Our partition algorithm requires that the pivot is the last element in the array.

    Algorithm for partitioning:
    pivot_index = median_of_three_pivot(arr, low, high)
    swap(pivot_index, high)

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(i, j)

    swap(i + 1, high)
    return i + 1

    Another approach (the one used in the course):
        swap(pivot_index, low)
        pivot = arr[low]
        i = low + 1

        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                swap(i, j)
                i += 1

        swap(low, i - 1)
        return i - 1
    '''
    pivot_index = median_of_three_pivot(arr, low, high)
    swap(pivot_index, low)
    pivot = arr[low]
    low_pointer = low + 1
    high_pointer = high

    while low_pointer <= high_pointer:
        if arr[low_pointer] < pivot:
            low_pointer += 1
        elif arr[high_pointer] > pivot:
            high_pointer -= 1
        else:
            swap(low_pointer, high_pointer)
            low_pointer += 1
            high_pointer -= 1

    swap(low, high_pointer)
    return high_pointer


def quick_sort(arr: list, low: int, high: int) -> list:
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr


def test_merge_sort(complexity: int = 0):
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

    for i in range(0, iterations):
        arr = [random.randint(0, size) for _ in range(size)]

        low = 0
        high = len(arr) - 1

        pivot_type = random.randint(0, 3)
        match pivot_type:
            case 0:
                pivot_type = first_pivot(arr)
            case 1:
                pivot_type = last_pivot(arr)
            case 2:
                pivot_type = median_of_three_pivot(arr, low, high)

        assert quick_sort(arr, low, high) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_merge_sort()
