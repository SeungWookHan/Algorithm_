from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # 브라운의 위치와 시간을 동시에 잡아주기 위함
    # 위치와 시간이 동시에 일치해야하지만 만났다고 할 수 있기에.
    visited = [{} for _ in range(200001)]
    # visited의 각 원소들은 각 시간 0초에 어느 곳을 갔는지 저장하기 위한 시간
    # visited[0] = { 2: True }, visited[1] = { 1:True, 3:True, 4:True} ...
    # 20만개의 딕셔너리를 배열에 넣음 [{}, {}, {}, ...]
    # visited[위치][시간]
    # visited[3] 에 5라는 키가 있냐? -> 3위치에 5초에 간적이 있나

    # 초기 위치는 2고 0초 이므로
    # 시간 0 1 -> visited[2] = { 0 : True }
    # 위치 2 1 -> visited[1] = { 1: True}
    #       3 -> visited[3] = { 1: True}
    #       4 -> visited[4] = { 1: True}

    # 시간이 2초일때 가능한 것은 다시
    # 시간 2 -> visited[2] = { 0 : True, 2: True }
    # 위치 0 -> visited[1] = { 1: True}
    #     2 -> visited[3] = { 1: True, 2: True}
    #     3 -> visited[4] = { 1: True, 2: True}
    #     4 -> visited[5] = { 2: True}
    #     5 -> visited[5] = { 6: True}
    #     6 -> visited[5] = { 8: True}
    #     8

    while cony_loc <= 200000:
        cony_loc += time #시간만큼 더해짐
        if time in visited[cony_loc]:
            return time
            # 이렇게 해준다면 이 시간대에 방문하게 된 것이므로 코니와 브라운이 만나게 된 시점을 알 수 있음

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 20000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
            # 모든 경우의 수 저장을 위한 각각 격우의 수 저장
        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!