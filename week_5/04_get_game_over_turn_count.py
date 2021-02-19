k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [
        [
            [] for _ in range(n) # 링크드 리스트를 위한
        ] for _ in range(n) # 4번 반복되서 큰 배열 안에 저장됨
    ] # 총 3차원 배열의 구성
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i) # 각 체스 말의 위치 저장
    # print(current_stacked_horse_map)
    # [
    #   [[0], [1], [2], []],
    #   [[], [], [], []],
    #   [[], [], [3], []],
    #   [[], [], [], []]
    #  ]
    turn_count = 1 # 턴의 실행 저장
    while turn_count <= 1000: # 최대 1000
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]
            # 범위 안에 안 있거나 그 칸이 파란색인 경우
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                # 반대로 한칸 이동
                # 동 -> 서, 서 -> 동, 북 -> 남, 남 -> 북
                new_d = get_d_index_when_go_back(d)

                # 방향을 옮겼으니 업데이트
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 방향을 뒤집어서 갈 곳도 파란색이거나 막혀있으면 안 감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 한 말이 이동할때 위에 올려져 있는 말이 함께 이동하고,
            # A 번 말이 이동하려는 칸이 흰색인 경우에는 그 칸으로 이동하고,
            # 이동하려는 칸에 이미 말이 있는 경우에는 가장 위에 A번 말을 올려놓고,
            # A 번 말에 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
            # 현재 어떻게 쌓여져 있는지 저장 필요
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])): # 기존에 존재하는 애들을 하나하나 꺼냄
                # 2가 이동한다고 치면 2, 3만 이동. 즉 자기자신의 인덱스보다 큰 애들만 데리고 감
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                    break
            # 만약에 이동할 칸이 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말이 쌓여있는 순서를 반대로 바꾼다.
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)

            # 만약에 이동할 칸이 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한칸 이동
            # 방향을 반대로 바꾼후에 이동하는 칸이 파란색인 경우에는 이동하지 않고 가만히 있고
            # 체스판을 벗어나는 경우 파란색과 같이 처리
            # 맨 앞에다 처리해주는 것이 좋고 빠름

            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                # 말이 이동했으면 말들의 순서대로 어느 위치, 방향을 보고 있는지 다시 저장 필요
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c

            # 턴이 진행되는 중 말이 4개 이상 쌓이는 순간 게임이 종료된다.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        turn_count += 1 # 반복을 할대마다 turn_count 올려줌

    return -1 # turn_count가 1000이 넘었는데도 아무것도 안되면 -1 반환


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다