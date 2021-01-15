input = "소주만병만주소"

# is_palindrom(string) -> 조건에 맞다면 -> is_palindrom(string[1:-1]
def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])


print(is_palindrome(input))