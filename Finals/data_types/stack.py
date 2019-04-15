class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        if self.head is None:
            self.head = Node(value, self.tail)
        else:
            self.head = Node(value, self.head)
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head
            self.head = self.head.next
            return ret_value

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

