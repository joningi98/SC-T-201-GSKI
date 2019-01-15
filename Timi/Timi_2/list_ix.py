import random


def insertion(length):
    my_list = ([0] * length)
    for ix, _ in enumerate(my_list):
        num = random.randint(1, 6)
        my_list[ix] = num
    print(my_list)


size = int(input("Enter size: "))
insertion(size)

# Keirslutíminn er O(n) þar sem lengdin af listanum ræður hversu oft for lykkjan keyrir
