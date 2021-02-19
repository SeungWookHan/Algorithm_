import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

# 여러개 중에서 M개를 고른뒤, 모든 치킨거리의 합이 가장 작게 되는 경우를 반환
# 여러 개 중에서 특정 개수를 뽑는 경우의 수, 모든 경우의 수를 다 구해야함 -> (조합)
def get_min_city_chicken_distance(n, m, city_map):
    # 치킨집과 집의 위치를 저장하기 위한 공간
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m)) # 조합 뽑음
    # print(chicken_location_m_combinations)
    # [([1, 2], [2, 2], [4, 4])]
    # 여기서는 튜플 하나만 담긴거임. 치킨집이 3개 밖에 없기에 3개 조합이면 1개 밖에 없기에..?

    # 최소 도시 치킨 거리 구하기
    min_distance_of_m_combinations = sys.maxsize # 애매한 수를 넣지 않고 시스템상 최대값

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0
        for home_r, home_c in home_location_list:
            # 각 집의 치킨거리 구하기
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )
            city_chicken_distance += min_home_chicken_distance
        # combination을 다 돌면서 최소 치킨 거리를 뽑아내야 하기 때문에 다시 한번 비교하여 최소값 넣어주기
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!