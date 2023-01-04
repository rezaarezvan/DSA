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


def test_selection_sort(complexity: int = 0):
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
        assert selection_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_selection_sort()
