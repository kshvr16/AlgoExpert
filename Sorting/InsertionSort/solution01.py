"""
Iterative method
Time - O(n^2) in worst case; O(n^2) in average case; O(n) in best case.
Space - O(1) --> as the insertion sort always sorts the array in place.
"""


def insertionSort(array):

    for idx in range(1, len(array)):
        for i in range(idx, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            else:
                break

    return array
