input = 20


def find_prime_list_under_number(number):
    result = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count <= 2:
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)