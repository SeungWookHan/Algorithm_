input = "hello my name is sparta"


# def find_max_occurred_alphabet(string):
#     alphabet_occurrence_array = [0] * 26
#     # 이 부분을 채워보세요!
#     for str in string:
#         if str.isalpha():
#             alphabet_occurrence_array[ord(str) - ord('a')] += 1
#     max_idx = alphabet_occurrence_array.index(max(alphabet_occurrence_array))
#     return chr(max_idx + 97)

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array


result = find_max_occurred_alphabet(input)
print(result)