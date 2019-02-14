class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DLL_Deque(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def push_front(self, data):
        new_node = Node(data, self.head.next, self.head)
        self.head.next = new_node
        new_node.next.prev = new_node
        self.size += 1

    def push_back(self, data):
        new_node = Node(data, self.tail, self.tail.prev)
        new_node.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def pop_front(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1

    def pop_back(self):
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.size -= 1

    def get_size(self):
        return self.size

    def walk_front(self):
        node = self.head.next
        while node.next is not Node:
            if node.next is not None:
                print(node.data)
                node = node.next

    def walk_back(self):
        node = self.tail.next
        while node.prev is not None:
            print(node.data)
            node = node.prev

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.next is not None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str


dl_list = DLL_Deque()

dl_list.push_front(1)
dl_list.push_front(2)
dl_list.push_front(3)
dl_list.push_back(56)


print(dl_list)

dl_list.pop_front()
dl_list.pop_back()
print(dl_list)

dl_list.walk_front()
dl_list.walk_back()



