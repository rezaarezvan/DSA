import random


def insertion_sort(arr: list) -> list:
    '''
    Sorts a list using the insertion sort algorithm.
    Algorithm:
        1. Have two parts of the array, the sorted part and the unsorted part.
        2. Begin with making the first element of the orignal array the sorted part.
        3. Compare each element of the unsorted part with the sorted part and insert it in the correct position.
    '''

    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1

        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

    return arr


def test_insertion_sort(complexity: int = 0):
    '''
    Tests the insertion sort algorithm.
    '''

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
        print(arr)
        assert insertion_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_insertion_sort()
