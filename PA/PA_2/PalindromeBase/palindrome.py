class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_to_screen(head):
    if head is not None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


def palindrome(head):

    def reverse_list(head):
        if head.next is None:
            return head
        node = reverse_list(head.next)
        head.next.next = head
        head.next = None
        return node

    def copy(head):
        if head is None:
            return None
        head2 = Node(head.data, head.next)
        head2.next = copy(head.next)
        return head2

    def compare_list(head1, head2):
        if head1 is None and head2 is None:
            return True
        if head1 is None or head2 is None:
            return False
        if head1.data != head2.data:
            return False
        if head1.data == head2.data:
            return compare_list(head1.next, head2.next)

    head2 = copy(head)
    new_head = reverse_list(head2)
    compare = compare_list(head, new_head)

    if compare:
        return True
    else:
        return False


if __name__ == "__main__":
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
