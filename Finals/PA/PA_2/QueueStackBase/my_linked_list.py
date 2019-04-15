class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        self.head = Node(value, self.head)
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def push_back(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        ret_val = self.head.data
        self.head = self.head.next
        self.size -= 1
        return ret_val

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

