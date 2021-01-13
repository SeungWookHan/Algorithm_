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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        try:
            prev_node = self.get_node(index - 1)
        except:
            pass
        now_node = node
        add = Node(value)
        if count == 0:
            add.next = now_node
            self.head = add
        else:
            add.next = now_node
            prev_node.next = add
        return


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()