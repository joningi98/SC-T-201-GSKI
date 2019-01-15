import random


def change_ix(my_list):
    num = random.randint(0, len(my_list) - 1)
    my_list[num] += 1
    print(my_list)
    return my_list


my_list = [3, 6, 1, 8, 3]
for _ in range(10):
    my_list = change_ix(my_list)

# þessi tíma flækja er O(1) því að stærð listanns er óháð tímanum
