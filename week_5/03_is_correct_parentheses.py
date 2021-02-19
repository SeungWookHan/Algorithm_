from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack: # 스택이 없을때 pop을 하면 에러가 나기에 조건문 필요. 스택이 비어있지 않고 존재할때
            stack.pop()
    return len(stack) == 0

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string

def seperate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char  # 하나하나 꺼내면서 u에다 붙임
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break  # 멈추는 이유는 u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없어야 된다고 했기 때문에
            # 즉 더 이상 쌍이 안생기기로 멈추도록 만들어줘야함
    v = ''.join(list(queue))  # '' 안에는 각 요소 중간중간에 무엇을 넣을지. 합쳐주는 것임
    # 나머지를 v에 넣어주는 것인데 왜 이게 균형잡힌 문자열이 될까? 왜냐면 애초에 균형잡힌 문자열만 넣어주기 때문이다.
    return u, v

def change_to_correct_parenthesis(string):
    # 1. 입력된 빈 문자열인 경우, 빈 문자열 반환
    if string == "":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리. 단 u는 "균형잡힌 괄호 문자열 더 이상 분리할수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # "(" ")" 개수가 같아야 한다.
    u, v = seperate_to_u_v(string)
    # 3. 문자열 u 가 "올바른 괄호 문자열"이라면
    # 문자열 v에 대해 1단계부터 다시 수행
    # 3-1. 수행한 결과 문자열을 u에 이어붙인뒤 반환
    # 즉 change_to_correct_parenthesis를 다시 수행(재귀적으로)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
    # 4-1. 빈 문자열에 첫 번째 문자로 ( 를 붙인다.
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과를 이어붙인다.
    # 4-3. ) 를 다시 붙인다.
    # 4-4. u의 첫번째 문자와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])
        # 주의할점: 첫번째 문자 마지막 문자를 제거하라고 했으니 인덱싱 필요

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!