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
        while node is not None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


class DLL_Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)


class DataList:
    def __init__(self):
        self.header = DLL_Node(None, None, None)
        self.tailer = DLL_Node(None, None, None)
        self.header.next = self.tailer
        self.tailer.prev = self.header
        self.size = 0

    def add_to_front(self, value):
        new_node = DLL_Node(value, self.header.next, self.header)
        self.header.next.prev = new_node
        self.header.next = new_node
        self.size += 1

    def add_to_back(self, value):
        new_node = DLL_Node(value, self.tailer, self.tailer.prev)
        self.tailer.prev.next = new_node
        self.tailer.prev = new_node
        self.size += 1

    def _remove(self, head, value):
        if head is self.tailer:
            return
        if head.data.x_type == value:
            head.prev.next = head.next
            head.next.prev = head.prev
            return self._remove(head.next, value)
        else:
            return self._remove(head.next, value)

    def get_all_of_type(self, type, remove_from_original=False):
        node = self.header.next
        new_dll = DataList()
        while node is not self.tailer:
            if node.data.x_type == type:
                new_dll.add_to_back(node)
            node = node.next
        if remove_from_original:
            self._remove(self.header.next, type)
        return new_dll

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node is not self.tailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


def count_value(node, value):
    if node is None:
        return 0
    if node.data == value:
        return 1 + count_value(node.next, value)
    else:
        return count_value(node.next, value)


def value_in_list(head, value):
    if head is None:
        return False
    if head.data == value:
        return True
    else:
        return value_in_list(head.next, value)


def _contains_help(head_1, head_2):
    if head_2 is not None:
        value = head_2.data
        if not value_in_list(head_1, value):
            return False
        else:
            return _contains_help(head_1, head_2.next)
    return True


def contains(head_1, head_2):
    return _contains_help(head_1, head_2) or _contains_help(head_2, head_1)


# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":
    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!
    """
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
    head_2 = SLL_Node(1, SLL_Node(2, SLL_Node(3)))
    print(contains(head, head_2))

    dll = DataList()
    dll.add_to_front(1)
    dll.add_to_front(2)
    dll.add_to_front(3)
    print(dll)
    dll.add_to_back(66)
    print(dll)
    """
    print("\nTesting get_all_of_type")
    dl1 = DataList()
    dl1.add_to_back(DataClass(1, "I: type 1"))
    dl1.add_to_back(DataClass(2, "O: type 2"))
    dl1.add_to_back(DataClass(3, "type 3 DataClass"))
    dl1.add_to_back(DataClass(1, "Other type 1"))
    dl1.add_to_back(DataClass(2, "More info: type 2"))
    dl1.add_to_back(DataClass(1, "Type 1 D.C."))
    print("dl1: " + str(dl1))
    dl2 = dl1.get_all_of_type(2)
    print("dl2: " + str(dl2))
    print("dl1: " + str(dl1))
    dl3 = dl1.get_all_of_type(1, True)
    print("dl3: " + str(dl3))
    print("dl1: " + str(dl1))