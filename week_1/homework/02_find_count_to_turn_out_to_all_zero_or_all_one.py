input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    case_zero = 0
    case_one = 0
    for idx in range(0, len(string)):
        if string[idx] == "0":
            if idx == 0:
                case_zero += 1
            else:
                if string[idx-1] == "0":
                    continue
                else:
                    case_zero += 1
        elif string[idx] == "1":
            if idx == 0:
                case_one += 1
            else:
                if string[idx - 1] == "1":
                    continue
                else:
                    case_one += 1
        else:
            print("0아니면 1만 입력해주세요")
            exit()
    return min(case_zero, case_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)