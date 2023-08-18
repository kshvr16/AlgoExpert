"""
Iterative method
Time - O(n)
Space - O(n)
"""


def runLengthEncoding(string):
    lst = []
    count = 1

    for idx in range(1, len(string)):
        prev_char = string[idx - 1]
        curr_char = string[idx]

        if prev_char == curr_char and count < 9:
            count += 1
        else:
            lst.append(str(count))
            lst.append(prev_char)
            count = 1

    lst.append(str(count))
    lst.append(string[-1])

    return ''.join(lst)
