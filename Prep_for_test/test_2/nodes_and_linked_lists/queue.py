class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def pop(self):
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


my_q = Queue()

my_q.push_back(1)
my_q.push_back(2)
my_q.push_back(3)
my_q.push_back(4)
my_q.push_back(5)

print(my_q)

print(my_q.pop())
print(my_q)