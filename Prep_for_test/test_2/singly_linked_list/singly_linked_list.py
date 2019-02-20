class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class Singly_linked_List:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.next = None
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def push_back(self, value):
        new_node = Node(value)
        if self.tail is None:
            new_node.next = None
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop_front(self):
        ret_value = self.head
        self.head = self.head.next
        self.size -= 1
        return ret_value

    def pop_back(self):
        node = self.head
        while node is not None:
            if node.next.next is None:
                ret_value = node.next
                node.next = None
                self.tail = node
                self.size -=1
                return ret_value
            node = node.next

    def insert_ordered(self, value):
        new_node = Node(value)
        node = self.head
        while node is not None:
            if node.data <= value <= node.next.data:
                new_node.next = node.next
                node.next = new_node
                self.size += 1
                break
            node = node.next

    def get_sum(self, head):
        if head.next is None:
            return head.data
        else:
            return head.data + self.get_sum(head.next)

    def get_size(self):
        return self.size

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
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


my_sll = Singly_linked_List()
my_sll.push_back(1)
my_sll.push_back(2)
my_sll.push_back(4)
print(my_sll)
my_sll.insert_ordered(3)
my_sll.insert_ordered(3)
print(my_sll)



