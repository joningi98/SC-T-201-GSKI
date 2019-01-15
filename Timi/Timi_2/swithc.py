import random


def switch(ix, my_list):
    new_list = my_list[:]
    new_list[ix] = my_list[ix + 1]
    new_list[ix + 1] = my_list[ix]
    print(new_list)

    x = random.randint(0, len(my_list) - 1)
    y = random.randint(0, len(my_list) - 1)

    some_list = new_list[:]
    some_list[x] = new_list[y]
    some_list[y] = new_list[x]
    print(some_list)


my_list = [3, 6, 1, 8, 3]
index = int(input())
switch(index, my_list)
