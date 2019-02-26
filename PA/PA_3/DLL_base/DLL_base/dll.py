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
        new_node = Node(value, self.curr_node, self.curr_node.prev)
        self.curr_node.prev.next = new_node
        self.curr_node.prev = new_node
        self.curr_node = new_node
        self.length += 1

    def remove(self):
        if self.curr_node is self.head or self.curr_node is self.tail:
            return
        ret_value = self.curr_node.data
        self.curr_node.prev.next = self.curr_node.next
        self.curr_node.next.prev = self.curr_node.prev
        self.curr_node = self.curr_node.next
        self.length -= 1
        return ret_value

    def remove_all(self, value):
        saved_curr = self.curr_node
        walk = self.head.next
        while walk != self.tail:
            if walk.data == value:
                self.curr_node = walk
                self.remove()
            walk = walk.next
        if saved_curr.data is value:
            self.move_to_pos(0)
        else:
            self.curr_node = saved_curr

    def reverse(self):
        for ix in range(self.length - 1):
            self.move_to_pos(ix + 1)
            new_node = self.remove()
            self.curr_node = self.head.next
            self.insert(new_node)
        self.move_to_pos(0)

    def sort(self):
        for _ in range(self.length):
            self.curr_node = self.head.next
            for i in range(self.length - 1):
                if self.curr_node.next is not None:
                    if self.curr_node.data > self.curr_node.next.data:
                        temp1 = self.curr_node.data
                        temp2 = self.curr_node.next.data
                        self.curr_node.data = temp2
                        self.curr_node.next.data = temp1
                    self.curr_node = self.curr_node.next
        self.move_to_pos(0)

    def get_value(self):
        if self.length < 0:
            self.length = 0
        return self.curr_node.data

    def move_to_next(self):
        if self.curr_node is not self.tail:
            self.curr_node = self.curr_node.next
        else:
            pass

    def move_to_prev(self):
        if self.curr_node is not self.head.next:
            self.curr_node = self.curr_node.prev
        else:
            pass

    def move_to_pos(self, index):
        if 0 <= index <= self.length:
            count = 0
            node = self.head.next
            while count < int(index):
                node = node.next
                count += 1
            self.curr_node = node

    def __len__(self):
        return self.length

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.data is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str
