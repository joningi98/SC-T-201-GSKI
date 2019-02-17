class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def pop_front(self):
        if self.size != 0:
            ret_data = self.head
            self.head = self.head.next
            self.size -= 1
            return ret_data

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = None
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_size(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
