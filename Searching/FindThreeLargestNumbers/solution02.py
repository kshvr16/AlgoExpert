"""
Iterative Approach
Optimized Solution --> Using a Single for loop
Time - O(n)
Space - O(1)
"""


def findThreeLargestNumbers(array):
    result = [float('-inf'), float('-inf'), float('-inf')]
    for num in array:
        # checking for position
        pos = -1
        for idx in range(3):
            if num > result[idx]:
                pos = idx

        # swapping and replacing the values in the result
        if pos == 0:
            result[0] = num
        if pos == 1:
            result[0] = result[1]
            result[1] = num
        if pos == 2:
            result[0] = result[1]
            result[1] = result[2]
            result[2] = num

    return result
