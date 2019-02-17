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


def palindrome(head):

    def palindrome_helper(head):
        if head.next is None:
            return head.data
        else:
            return str(head.data) + palindrome_helper(head.next)

    palin_word = list(palindrome_helper(head))
    if palin_word == list(reversed(palin_word)):
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
