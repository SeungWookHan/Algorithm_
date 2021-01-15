input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n-1-i]: #인덱스기 때문에 -1 해주는 것
            return False
    return True


print(is_palindrome(input))