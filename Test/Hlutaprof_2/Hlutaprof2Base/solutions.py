class DataClass:
    # USE THIS IMPLEMENTATION OF DATACLASS UNCHANGED
    def __init__(self, x_type, x_information):
        self.x_type = x_type
        self.x_information = x_information

    def __str__(self):
        return "{" + str(self.x_type) + ": " + str(self.x_information) + "}"


class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


def count_value(head, value):
    if head is None:
        return 0
    if head.data == value:
        return 1 + count_value(head.next, value)
    else:
        return 0 + count_value(head.next, value)


def contains_all(head1, head2):
    node_1 = head1
    node_2 = head2
    while True:
        if node_1 is None:
            node_1 = reverse_list(head)
        if node_2 is None:
            return True
        if node_1.data == node_2.data:
            node_2 = node_2.next
        node_1 = node_1.next

    # if head1.next is None and head1.data != head2.data:
    #    head1 = reverse_list(head1)
    # if head1.next is None and head1.data == head2.data:
    #    head1 = reverse_list(head1)
    #    contains_all(head1, head2)
    # if head1.data == head2.data:
    #    contains_all(head1.next, head2.next)
    #    contains_all(head1, head2)
    # if head1.data != head2.data:
    #    contains_all(head1.next, head2)
    # if head2 is None:
    #    return True
    # else:
    #    return False


def reverse_list(head):
    if head.next is None:
        return head
    node = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DataList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_front(self, value):
        new_node = Node(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node

    def add_back(self, value):
        new_node = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def remove(self, target):
        current_node = self.head.next
        while current_node.next is not None:
            if current_node.data.x_type == target:
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
            current_node = current_node.next

    def get_all_of_type(self, type, remove_from_original=False):
        new_list = DataList()
        curr_node = self.head.next
        while curr_node.next is not None:
            if curr_node.data.x_type == type:
                new_list.add_back(curr_node.data)
            curr_node = curr_node.next
        if remove_from_original:
            self.remove(type)

        return new_list

    def __str__(self):
        ret_str = ""
        node = self.head.next
        while node.data is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":
    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("DataClass example:")
    dc = DataClass(2, "A string with some information for type 2")
    print(str(dc))
    dc = DataClass(3, "A string with information for type 3 DataClass")
    print(str(dc))
    dc = DataClass(2, "More information for a type 2 D.C.")
    print(str(dc))

    print("Singly-linked node example:")
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    print(str(head))

    new_head = SLL_Node(1, SLL_Node(2, SLL_Node(1, SLL_Node(1, SLL_Node(5)))))

    print("# of 1: " + str(count_value(new_head, 1)))
    print("# of 4: " + str(count_value(new_head, 4)))
    print("# of 5: " + str(count_value(new_head, 5)))

if __name__ == "__main__":
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    head1 = SLL_Node(5, SLL_Node(2, SLL_Node(1)))
    head2 = SLL_Node(5, SLL_Node(2, SLL_Node(0)))
    head3 = SLL_Node(6, SLL_Node(1, SLL_Node(2)))

    print(contains_all(head, head1))
    print(contains_all(head, head2))
    print(contains_all(head, head3))


"""
if __name__ == "__main__":
    head = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5)))))
    head1 = SLL_Node(5, SLL_Node(2, (SLL_Node(1))))
    print(contains_all(head, head1))

if __name__ == "__main__":
    my_dll = DataList()
    my_dll.add_front(1)
    my_dll.add_back(55)
    my_dll.add_front(66)
    print(my_dll)


if __name__ == "__main__":
    print("\nTesting get_all_of_type")
    dll = DataList()
    dll.add_back(DataClass(1, "I: type 1"))
    dll.add_back(DataClass(2, "O: type 2"))
    dll.add_back(DataClass(3, "type 3 DataClass"))
    dll.add_back(DataClass(1, "Other type 1"))
    dll.add_back(DataClass(2, "More info: type 2"))
    dll.add_back(DataClass(1, "Type 1 D.C"))
    print("dll: " + str(dll))
    dl2 = dll.get_all_of_type(2)
    print("dll2: " + str(dl2))
    print("dll2: " + str(dll))
    dl3 = dll.get_all_of_type(1, True)
    print("dl3: " + str(dl3))
    print("dl1: " + str(dll))

"""
