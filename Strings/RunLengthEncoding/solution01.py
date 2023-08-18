"""
Iterative method
Time - O(n)
Space - O(n)
"""


def runLengthEncoding(string):
    run_length = []

    count = 1
    prev_char = string[0]
    for idx in range(1, len(string)):
        curr_char = string[idx]
        if curr_char == prev_char and count < 9:
            count += 1
        else:
            run_length.append(str(count))
            run_length.append(prev_char)
            count = 1
        prev_char = curr_char

    run_length.append(str(count))
    run_length.append(prev_char)

    return ''.join(run_length)
