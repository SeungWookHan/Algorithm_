shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort() # ['떡볶이', '만두', '사이다', '오뎅', '콜라']
    orders.sort() # ['만두', '오뎅', '콜라']
    total_correct = []
    for order in orders:
        correct = False
        current_min = 0
        current_max = len(menus) - 1
        current_guess = (current_min + current_max) // 2
        while current_min <= current_max:
            if menus[current_guess] == order:
                correct = True
                break
            elif menus[current_guess] < order:
                current_min = current_guess + 1
            else:
                current_max = current_guess - 1
            current_guess = (current_min + current_max) // 2
        menus = menus[current_guess+1:] # 그 다음거는 무조건 이거 이상이기에 슬라이싱
        if correct == False:
            return False
    return True



result = is_available_to_order(shop_menus, shop_orders)
print(result)