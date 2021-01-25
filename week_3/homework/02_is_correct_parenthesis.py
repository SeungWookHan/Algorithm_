# 코드 스니펫
s = "(())()("


def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i) # 어떤 값이 들어가도 상관 없음
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!