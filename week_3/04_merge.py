array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge(array1, array2):
    array_c = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            array_c.append(array1[array1_index])
            array1_index += 1
        else:
            array_c.append(array2[array2_index])
            array2_index += 1
    if array1_index == len(array1): # 남는걸 다 넣어주는 코드, array1이 끝났을 때
        while array2_index < len(array2):
            array_c.append(array2[array2_index])
            array2_index += 1
    if array2_index == len(array2):  # 남는걸 다 넣어주는 코드, array2이 끝났을 때
        while array1_index < len(array1):
            array_c.append(array1[array1_index])
            array1_index += 1
    return array_c

print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!