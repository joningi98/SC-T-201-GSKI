
class SLL_Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# Solution I
def rec_avg(head, curr_avg, item_num):
    if head == None:
        return curr_avg
    return rec_avg(head.next, (curr_avg * (item_num - 1) + head.data) / item_num, item_num + 1)

def average_of_list(head):
    return rec_avg(head, 0, 1)

# # Solution II
# def rec_avg(head):
#     if head == None:
#         return 0, 0
#     total, count = rec_avg(head.next)
#     return total + head.data, count + 1

# def average_of_list(head):
#     total, count = rec_avg(head)
#     return total / count

# # Solution III
# def rec_avg(head):
#     if head == None:
#         return 0, 0
#     elif head.next == None:
#         return head.data, 1
#     curr_avg, count = rec_avg(head.next)
#     return (curr_avg * count + head.data) / (count + 1), count + 1

# def average_of_list(head):
#     avg, _ = rec_avg(head)
#     return avg

if __name__ == "__main__":
    # MAKE BETTER TESTS!
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(7, SLL_Node(5, None))))))
    print(average_of_list(SLL_Node(1, SLL_Node(3, SLL_Node(2, SLL_Node(4, None))))))
    print(average_of_list(SLL_Node(7, SLL_Node(5, SLL_Node(6, None)))))