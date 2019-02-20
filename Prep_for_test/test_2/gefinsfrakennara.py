class Node:
    def __init__(self, next, data):
        self.next = next
        self.data = data


def push_front(head, val):
    return Node(head, val)


def push_back(head, val):
    if head == None:
        return Node(head, val)
    return Node(push_back(head.next, val), head.data)


def len_list(head):
    if head == None:
        return 0
    else:
        return 1 + len_list(head.next)


def insert_node(head, val):
    if head == None:
        return Node(head, val)
    if head.data >= val:
        return Node(head, val)
    return Node(insert_node(head.next, val), head.data)


def print_list(head):
    if head == None:
        print()
    else:
        print(head.data, end=' ')
        print_list(head.next)


head = None
count = 0
for x in range(10):
    head = push_back(head, x)

print_list(head)
print(len_list(head))
insert_node(head, 10)
print_list(head)
print(len_list(head))

# ● Implement an operation that takes a node (head of an ordered list) and a value (data) as
# parameters and adds the item in the correct location in the list, so that it is still ordered.
# ○ This should be able to take an empty list, so that you can use it to fully populate
# an ordered list.
# ○ Is this one more elegant when done recursively?


# ● Implement a function that takes a node (head) as a parameter and returns a node, the
# head of a list that has the same items as the previous list, but in reverse order.
# ○ Can you do this by using all the same nodes, not by making new ones?
# ■ Only change their next links.
# ■ Could you do that with previous operations as well (i.e. merge_lists)?
# ● Implement an operation (merge_lists) that takes two nodes (the heads of two ordered
# lists) as parameters and returns one node, the head of a list which has all the elements
# from the other two in one ordered list.
# ○ Make this one recursive!
# ○ This is fairly advanced. Skip ahead, if having trouble.
# ● Implement merge_sort on a singly-linked list, splitting the list recursively into halves until
# each part has only 1 or 0 items, then using merge_lists to reconnect them ordered.
# ○ This is advanced. It’s OK to finish the linked_list class assignment below first.
# ○ It can be tricky when a list is down to 2 items. Make sure the split happens
# between them, not behind the second one, as that will give another list of length
# 2, which results in endless recursion. Video lecture is not definitive enough :)
