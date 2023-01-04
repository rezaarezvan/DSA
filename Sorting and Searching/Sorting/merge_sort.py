import random
import merge_lists as ml


def merge_sort(arr: list) -> list:
    '''
    Algorithm:
        1. Split the array into two halves
        2. Recursively sort the two halves
        3. Merge the two sorted halves
    '''

    # Base case, if the array is empty or has one element, it is sorted
    if len(arr) < 2:
        return arr[:]

    else:
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return ml.merge_lists(left, right)


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
        assert merge_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_merge_sort()
