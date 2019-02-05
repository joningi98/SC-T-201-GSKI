class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pop_front(self):
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        self.size -= 1

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

    def pop_back(self):
        pass

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str


linked_list = LinkedList()

for i in range(1, 6):
    linked_list.push_back("String" + str(i))

linked_list.pop_front()
print(linked_list.get_size())
print(linked_list)
