def natural_recur(curr_val, max_val):
    if curr_val == max_val:
        return str(curr_val)
    else:
        return str(curr_val) + " " + natural_recur(curr_val + 1, max_val) + " " + str(curr_val)


def natural_fb(val):
    if val < 1:
        return ""
    return natural_recur(1, int(val))


def natural_bf(val):
    if val < 1:
        return ""
    elif val == 1:
        return "1"
    return str(val) + " " + natural_bf(val - 1) + " " + str(val)


def sum_of_even_recur(min, max):
    if min > max:
        return 0
    return min + sum_of_even_recur(min + 2, max)


def sum_of_even(min, max):
    if min % 2 == 1:
        min += 1
    return sum_of_even_recur(min, max)


def sum_of_odd_recur(min, max):
    if min > max:
        return 0
    return min + sum_of_odd_recur(min + 2, max)


def sum_of_odd(min, max):
    if min % 2 == 0:
        min += 1
    return sum_of_odd_recur(min, max)


def sum_of_threes_recur(x):
    if x <= 0:
        return 0
    return x + sum_of_threes_recur(x - 3)


def sum_of_threes(x):
    if x % 3 == 0:
        x -= 3
    else:
        x -= (x % 3)
    return sum_of_threes_recur(x)


def is_in_list(lis, x):
    if len(lis) == 0:
        return False
    if lis[0] == x:
        return True
    return is_in_list(lis[1:], x)


def raise_items_recur(lis, index):
    if (index < 0):
        return
    lis[index] += 1
    raise_items_recur(lis, index - 1)


def raise_items(lis):
    return raise_items_recur(lis, len(lis) - 1)


def sum_of_items(lis):
    if len(lis) == 0:
        return 0
    return lis[0] + sum_of_items(lis[1:])
