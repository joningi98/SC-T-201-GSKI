import random


def make_list():
    size = random.randint(1, 6)
    my_list = []
    for _ in range(size):
        my_list.append(random.randint(0, 9))
    return my_list


def order_list(the_list):
    new_list = []
    for _ in range(len(the_list)):
        new_list.append(min(the_list))
        the_list.remove(min(the_list))
    return new_list


def main():
    my_list = make_list()
    print("Unsorted list: {}".format(my_list))
    new_list = order_list(my_list)
    print("Sorted list: {}".format(new_list))


main()
