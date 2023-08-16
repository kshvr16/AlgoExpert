"""
Iterative method
Time - O(n^2) in worst case; O(n^2) in average case; O(n) in best case.
Space - O(1) --> as the bubble sort always sorts the array in place.
"""


def bubbleSort(array):
    swapped = True
    length = len(array) - 1

    while swapped:
        swapped = False
        for idx in range(length):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swapped = True
        length -= 1

    return array
