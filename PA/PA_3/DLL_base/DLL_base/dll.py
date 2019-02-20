
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DLL:
    def __init__(self):
        self.tail = Node()
        self.head = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.curr_node = self.tail
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        new_node.prev = self.curr_node.prev
        new_node.next = self.curr_node
        self.curr_node.prev.next = new_node
        self.curr_node.prev = new_node
        self.curr_node = new_node
        self.length += 1

    def remove(self):
        if self.curr_node.data is None:
            pass
        if self.curr_node.data is not None:
            self.curr_node = self.curr_node.next
            self.curr_node.prev = self.curr_node.prev.prev
            self.curr_node.prev.next = self.curr_node
            self.length -= 1

    def get_value(self):
        return self.curr_node.data

    def move_to_next(self):
        self.curr_node = self.curr_node.next

    def move_to_prev(self):
        self.curr_node = self.curr_node.prev

    def move_to_pos(self, position):
        if 0 <= position <= self.length:
            node_pos = 0
            node = self.head.next
            while node.next is not None:
                if node_pos == position:
                    self.curr_node = node
                node_pos += 1
                node = node.next

    def __len__(self):
        return self.length

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.data is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
