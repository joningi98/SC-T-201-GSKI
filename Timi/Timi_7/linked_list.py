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

    def pop_front(self):
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def pop_back(self, head):
        if head.next.next is None:
            head.next = None
        else:
            self.pop_back(head.next)

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = None
        else:
            new_node.next = self.head
            self.head = new_node

    def get_size(self, head):
        if head is None:
            return 0
        else:
            return 1 + self.get_size(head.next)

    def sum_of_data(self, head):
        if head is None:
            return 0
        else:
            return head.data + self.sum_of_data(head.next)

    def insert_ordered(self, head, data):
        if head is None or head.data > data:
            return Node(data, head)
        head.next = self.insert_ordered(head.next, data)
        return head

    def reverse_list(self, head):
        if head.next is None:
            return head
        ret_node = self.reverse_list(head.next)
        head.next.next = head
        head.next = None
        return ret_node

    def __str__(self):
        ret_str = ""
        node = self.head
        while node is not None:
            ret_str += str(node.data) + "\n"
            node = node.next
        return ret_str


linked_list = LinkedList()

for i in range(1, 6):
    linked_list.push_back(i)

print(linked_list)
linked_list.head = linked_list.insert_ordered(linked_list.head, 3)
print(linked_list)
linked_list.pop_back(linked_list.head)
print(linked_list)
linked_list.head = linked_list.reverse_list(linked_list.head)
print(linked_list)

