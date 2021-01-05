input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurence = alphabet_occurrence_array[index]

        if alphabet_occurence > max_occurence:
            max_alphabet_index = index
            max_occurence = alphabet_occurence
    return chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)