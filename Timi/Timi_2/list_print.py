

def display_list(my_list):
    for ix, x in enumerate(my_list):
        if ix == len(my_list) - 1:
            print("{}".format(x), end="")
        else:
            print("{},".format(x), end="")


my_list = [3, 6, 1, 8, 3]
display_list(my_list)

# Keirslutíminn er O(n) þar sem lengdin af listanum ræður hversu oft for lykkjan keyrir
