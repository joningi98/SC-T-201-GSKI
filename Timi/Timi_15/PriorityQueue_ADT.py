class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedListPriority:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.next = self.__head
        self.__head = new_node

    def pop_front(self):
        ret_data = self.__head.data
        self.__head = self.__head.next
        return ret_data

    def insert_ordered(self, value):
        new_node = Node(value)
        node = self.__head
        while node is not None:
            if node.data > value > node.next.data:
                new_node.next = node.next
                node.next = new_node
                break
            node = node.next

    def __str__(self):
        ret_str = ""
        node = self.__head
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


ll = LinkedListPriority()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(5)
print(ll)
ll.insert_ordered(4)
print(ll)