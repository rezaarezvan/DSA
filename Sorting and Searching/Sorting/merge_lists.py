import random


def merge_lists(arr1: list, arr2: list) -> list:
    '''
    Merges two *sorted* lists into one list, keeping the sorted order.
    Algortihm:
        1. We compare two elements to each other in both merge_lists
        2. We pick the smallest of these two and append it to the resulting list.
        3. If we length of the input arrays differ, we always choose the one with the shortest length to iterate over *both*.
        4. Once the shortest input array has ended we can append the rest of the resulting list.

    '''
    result = []
    index_1 = 0
    index_2 = 0

    while index_1 < len(arr1) and index_2 < len(arr2):
        if arr1[index_1] <= arr2[index_2]:
            result.append(arr1[index_1])
            index_1 += 1
        else:
            result.append(arr2[index_2])
            index_2 += 1

    # In the case
    while index_1 < len(arr1):
        # NOTE: We could just use .extend, but that's a python thing :)
        result.append(arr1[index_1])
        index_1 += 1

    while index_2 < len(arr2):
        # NOTE: We could just use .extend, but that's a python thing :)
        result.append(arr2[index_2])
        index_2 += 1

    return result


def test_insertion_sort():
    for i in range(1, 101):

        # To make sure we can merge lists of different length
        l1 = random.randint(1, 100)
        l2 = random.randint(1, 100)

        arr1 = [random.randint(0, 100) for _ in range(l1)]
        arr2 = [random.randint(0, 100) for _ in range(l2)]

        # Make sure both lists are sorted
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)

        assert merge_lists(arr1, arr2) == sorted(arr1 + arr2)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_insertion_sort()
