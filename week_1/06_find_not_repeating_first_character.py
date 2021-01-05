input = "abadabac"


# def find_not_repeating_first_character(string):
#     dict = {}
#     for char in string:
#         if dict.get(char):
#             dict[char]=dict.get(char) + 1
#         else:
#             dict[char] = 1
#     result = [i for i, x in dict.items() if x ==1]
#     return result[0]
def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]
        if alphabet_occurence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char

result = find_not_repeating_first_character(input)
print(result)