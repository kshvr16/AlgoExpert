"""
Recursive method
Time - O(n)
Space - O(n)
Note: As it is a recursive methods, it's going to use the stack memory space for storing recursive calls.
"""


def isPalindrome(string):
    return checkForPalindrome(string, left=0, right=len(string) - 1)


def checkForPalindrome(string, left, right):
    if left > right:
        return True
    if string[left] == string[right]:
        return checkForPalindrome(string, left + 1, right - 1)
    if string[left] != string[right]:
        return False
