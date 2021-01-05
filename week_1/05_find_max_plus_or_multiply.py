input = [0, 3, 5, 6, 1, 2, 4]


# def find_max_plus_or_multiply(array):
#     result = 0
#     for i in range(0, len(array)):
#         try:
#             if array[i] == 0 or array[i+1] == 0 or array[i] == 1 or array[i+1] == 1:
#                 result += array[i] + array[i+1]
#             else:
#                 result += array[i] * array[i+1]
#         except:
#             return result

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)