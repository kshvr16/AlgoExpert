"""
Recursive method
Time - O(log(n))
Space - O(log(n))
Note: As it is a recursive methods, it's going to use the stack memory space for storing recursive calls.
"""


def binarySearch(array, target):
    return helper(array, target, 0, len(array) - 1)


def helper(array, target, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            return helper(array, target, mid + 1, right)
        if array[mid] > target:
            return helper(array, target, left, mid - 1)
