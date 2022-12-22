import random


def linear_search(arr: list, target: int) -> int:
    '''
    Algorithm:
    '''

    '''
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
    '''

    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


def test_linear_search(complexity: int = 0):
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

        assert linear_search(arr, target) == arr.index(target)

        print(f"Test {i} passed")


if __name__ == "__main__":
    test_linear_search()
