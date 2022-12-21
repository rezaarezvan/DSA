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


def test_insertion_sort():
    for i in range(1, 101):
        arr = [random.randint(0, 100) for _ in range(100)]
        assert insertion_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_insertion_sort()
