class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DLL:
    def __init__(self):
        self.header = Node()
        self.tailer = Node()
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0

    def push_front(self, value):
        new_node = Node(value, self.header.next, self.header)
        self.header.next.prev = new_node
        self.header.next = new_node
        self.size += 1

    def push_back(self, value):
        new_node = Node(value, self.tailer, self.tailer.prev)
        self.tailer.prev.next = new_node
        self.tailer.prev = new_node
        self.size += 1

    def pop_front(self):
        self.header.next.next.prev = self.header
        self.header.next = self.header.next.next
        self.size -= 1

    def pop_back(self):
        self.tailer.prev.prev.next = self.tailer
        self.tailer.prev = self.tailer.prev.prev

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node is not self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


dll = DLL()

dll.push_front(1)
dll.push_front(2)
dll.push_front(3)
dll.push_back(4)
print(dll)
dll.pop_front()
print(dll)
dll.pop_back()
print(dll)
