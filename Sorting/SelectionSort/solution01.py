"""
Iterative method
Time - O(n^2) in worst case; O(n^2) in average case; O(n) in best case.
Space - O(1) --> as the selection sort always sorts the array in place.
"""


def selectionSort(array):
    for i in range(len(array)):
        idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx]:
                idx = j
        array[i], array[idx] = array[idx], array[i]

    return array
