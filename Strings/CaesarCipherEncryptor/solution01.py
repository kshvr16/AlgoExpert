"""
Iterative method
Time - O(n)
Space - O(n)
"""


def caesarCipherEncryptor(string, key):
    mapper = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z']
    cipher_lst = []
    for char in string:
        char_num = mapper.index(char)
        new_char_num = char_num + key
        new_char_num %= 26
        cipher_lst.append(mapper[new_char_num])

    return "".join(cipher_lst)
