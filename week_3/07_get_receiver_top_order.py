top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # [0, 0, 0, 0, 0]
    while heights: # heights가 빈 상태가 아닐때 까지
        height = heights.pop()
        for idx in range(len(heights) -1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
                # 7의 높이를 가진 레이저에 부딪히는 것을 알았기에 해당 7의 인덱스인 4를 answer의 맨 마지막 원소에 넣어야 함.
                # idx + 1은 위치를 알려주길 원했기 때문
                # answer에 넣으려면 하나 뺀것에 대한 것 더하기 1 이므로 인덱스로 해서 현재 나와 있는 스택의 길이로 함.
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!