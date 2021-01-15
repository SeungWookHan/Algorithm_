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

    def get_node_linked_list(self, index):
        pass

    def get_kth_node_from_last(self, k):
        k = k-1
        count = 0
        cur = self.head
        while cur is not None:
            if count == k:
                return cur
            else:
                cur = cur.next
                count += 1
        if cur == None: # 예외처리
            exit()


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!