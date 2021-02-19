from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 위치
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# 방문 저장 여부 visited를 만들어야 함
# 공이 2개 이라 4차원 배열을 사용!
# visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
# 4차원 배열이 공간낭비가 아닐까 생각이 들지만  보드의 행 열 길이가 3 <= x <= 10 이기에 문제 없음!

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    # game_map도 받는 이유는 이동하려는 곳이 벽인지 구멍인지 알아야 하기 때문에

    move_count = 0
    while game_map[r + diff_r][c + diff_c] != "#" and game_map != "0":
    # 이동할 곳이 벽이 아닐때까지와 구멍일때
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count

def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    # row 는 n, col은 m 즉 n, m, n, m 이기에 그 순서대로 초기화
    # print(visited)
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque()
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j
    # 탐색을 10번까지만 할 수 있음
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    # 큐룰 이용한 탐색
    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        # 이동에 대한 모든 경우
        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O':
                continue # 블루가 먼저 들어갔기에
            if game_map[next_red_row][next_red_col] == 'O':
                return True # 레드가 먼저 들어갔다면

            # 블루와 레드는 만날 수가 없음 끝까지 가는 도중에 동일 선상에 있으면 안됨
            # ..BR 일때 다 왼쪽 끝으로 옮기면
            # B..
            # R
            # 이런 구조가 되는데 이렇게 되면 안되기에 BR..으로 되야함. 옮긴 다음에 후보정을 해줘야함
            # 벽에 다다랐을때 두개의 움직은 거리를 비교해서 조금 움직인애는 그대로 끝에 있고 더 많이 움직인애는 한칸 떨어지게 함
            # 위의 예에서 B는 2번 이동, R은 3번 이동
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            # BFS 방식이기에 현재 방문하지 않았다면 해당 위치를 다시 큐에 넣고 반복
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다