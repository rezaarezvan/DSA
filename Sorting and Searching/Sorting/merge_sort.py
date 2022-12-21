import random
import merge_lists as ml


def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr[:]
    else:
        mid = len(arr) // 2

        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return ml.merge_lists(left, right)


def test_merge_sort():
    for i in range(1, 101):
        arr = [random.randint(0, 100) for _ in range(10)]
        assert merge_sort(arr) == sorted(arr)
        print(f"Test {i} passed")


if __name__ == "__main__":
    test_merge_sort()
