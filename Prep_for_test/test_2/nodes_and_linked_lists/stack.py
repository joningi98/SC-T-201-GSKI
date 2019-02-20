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

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = None
        else:
            new_node.next = self.head
        self.head = new_node

    def pop(self):
        self.head = self.head.next

    def display_list(self, node):
        if node.next is None:
            return str(node.data)
        else:
            return str(node.data) + " " + self.display_list(node.next)

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


my_ll = Stack()
my_ll.push_front(1)
my_ll.push_front(2)
my_ll.push_front(3)
my_ll.push_front(4)
print(my_ll.display_list(my_ll.head))
my_ll.pop()
print(my_ll)