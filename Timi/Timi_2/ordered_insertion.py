import random


def insertion():
    my_list = [1, 2, 4, 5, 6]
    num = random.randint(1, 6)
    for ix, _ in enumerate(my_list):
        if num < my_list[ix]:
            my_list.append(my_list[ix])
            my_list[ix] = num
            break
        else:
            continue
    print(my_list)


insertion()
