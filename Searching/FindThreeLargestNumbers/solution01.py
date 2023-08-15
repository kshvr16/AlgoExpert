"""
Iterative Approach
Basic Solution --> Using three for loops but still keeps the time complexity to O(n)
Time - O(n)
Space - O(1)
"""


def findThreeLargestNumbers(array):
    largest = float("-Inf")
    largest_pos = -1

    second_largest = float("-Inf")
    second_largest_pos = -1

    third_largest = float("-Inf")
    third_largest_pos = -1

    # first largest
    for idx in range(len(array)):
        if array[idx] > largest:
            largest = array[idx]
            largest_pos = idx

    # second largest
    for idx in range(len(array)):
        if idx != largest_pos and array[idx] > second_largest:
            second_largest = array[idx]
            second_largest_pos = idx

    # third largest
    for idx in range(len(array)):
        if idx != largest_pos and idx != second_largest_pos and array[idx] > third_largest:
            third_largest = array[idx]
            third_largest_pos = idx

    return [third_largest, second_largest, largest]
