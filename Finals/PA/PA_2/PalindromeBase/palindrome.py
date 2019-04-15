class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_to_screen(head):
    if head is not None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


def _copy(head):
    if head is None:
        return None
    else:
        head2 = Node(head.data, head.next)
        head2.next = _copy(head.next)
        return head2


def _reverse_list(head):
    if head.next is None:
        return head
    node = _reverse_list(head.next)
    head.next.next = head
    head.next = None
    return node


def _compare(head_1, head_2):
    if head_1.data != head_2.data:
        return False
    if head_1.next is None and head_2.next is None:
        return True
    if head_1.next is None or head_2.next is None:
        return False
    else:
        return _compare(head_1.next, head_2.next)


def palindrome(head):
    copy_head = _copy(head)
    rev_head = _reverse_list(copy_head)
    return _compare(head, rev_head)


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
