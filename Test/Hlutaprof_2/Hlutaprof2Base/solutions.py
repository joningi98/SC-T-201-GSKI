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


class DataList:
    pass  # REMOVE THIS LINE WHEN YOU START IMPLEMENTING


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
