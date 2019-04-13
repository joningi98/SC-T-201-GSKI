class SLL_Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


# IMPLEMENT THIS
def average_of_list(head):
    return average_sum(head) / average_len(head)


def average_sum(head):
    if head is None:
        return 0
    else:
        return int(head.data) + average_sum(head.next)


def average_len(head):
    if head is None:
        return 0
    else:
        return 1 + average_len(head.next)


if __name__ == "__main__":
    # MAKE BETTER TESTS!
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(7, SLL_Node(5, None))))))
    print(average_of_list(SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, None))))))
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(6, None)))))
