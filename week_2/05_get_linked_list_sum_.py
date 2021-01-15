class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    list_1 = []
    list_2 = []
    sum = []
    cur_1 = linked_list_1.head
    cur_2 = linked_list_2.head
    while cur_1 is not None:
        list_1.append(cur_1.data)
        cur_1 = cur_1.next
    while cur_2 is not None:
        list_2.append(cur_2.data)
        cur_2 = cur_2.next
    for num1, num2 in zip(list_1, list_2):
        sum.append(num1+num2)
    return sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))