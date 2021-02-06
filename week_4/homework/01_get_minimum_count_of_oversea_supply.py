import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    current_day_index = 0 # 오늘이 며칠인지에 따라서 가지고 올 수 있는 supply 수가 다르기에
    max_heap = [] # 현재 공급량이 떨어지지 않는 선에서 가장 많은 공급량을 가지고 올 수 있게

    while stock < k:
        # date를 기준으로 반복. 왜냐면 지금 내가 재고가 바닥난 상황인지 아닌지를 알기 위함
        for date_index in range(current_day_index, len(dates)):
            if dates[date_index] <= stock: # 현재 스톡이 4고 요일이 10이면 10 < 4라서 조건이 안 맞기에
                heapq.heappush(max_heap, -supplies[date_index])
            else:
                current_day_index = date_index
                break
        answer += 1
        stock += -heapq.heappop(max_heap)
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))