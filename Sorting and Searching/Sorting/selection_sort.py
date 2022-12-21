import random


def selection_sort(arr: list) -> list:
    '''
    Sorts a list of numbers using the selection sort algorithm.
    Algorithm:
        1. Find the minimum element in the list
        2. Swap it with the first element
        3. Repeat the process for the remaining elements
    '''

    def swap(i, j):
        '''
        Auxiliary function to swap two elements in a list
        '''
        (arr[i], arr[j]) = (arr[j], arr[i])

    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        swap(i, min)
    return arr


def test_selection_sort():
    for i in range(1, 101):
        arr = [random.randint(0, 100) for _ in range(100)]
        assert selection_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_selection_sort()
