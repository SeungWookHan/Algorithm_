input = [3, 5, 6, 1, 2, 4]


# def is_number_exist(number, array):
#     if number in array:
#         return True
#     return False

def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True
    return False

result = is_number_exist(3, input)
print(result)