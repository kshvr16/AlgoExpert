"""
Iterative method
Time - O(n^2) in worst case; O(n^2) in average case; O(n) in best case.
Space - O(1) --> as the bubble sort always sorts the array in place.
"""


def bubbleSort(array):
    swapped = True

    while swapped:
        swapCount = 0
        for idx in range(len(array) - 1):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
                swapCount += 1
        if swapCount == 0:
            swapped = False

    return array
