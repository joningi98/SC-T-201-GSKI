def natural_recur(value, max_value):
    if value == max_value:
        return str(value)
    else:
        return "{} {} {}".format(value, natural_recur(value + 1, max_value), value)


def natural_fb(number):
    if number < 1:
        return ""
    else:
        return natural_recur(1, int(number))


print(natural_fb(6))


def sum_of_list(my_list):
    if len(my_list) == 0:
        return 0
    else:
        return my_list[0] + sum_of_list(my_list[1:])


some_list = [5, 5]

print("Sum of lists")
print(sum_of_list(some_list))


def sum_of_even_helper(curr_num, min_num, max_num):
    if curr_num == min_num:
        if curr_num % 2 == 0:
            return curr_num
        else:
            return 0
    if curr_num % 2 == 0:
        return curr_num + sum_of_even_helper(curr_num - 1, min_num, max_num)
    else:
        return sum_of_even_helper(curr_num - 1, min_num, max_num)


def sum_of_even(min_num, max_num):
    return sum_of_even_helper(max_num, min_num, max_num)


print("Sum of even")
print(sum_of_even(3, 8))


def raise_by_one(my_list):
    if len(my_list) == 1:
        return [int(my_list[0]) + 1]
    else:
        return [int(my_list[0]) + 1] + raise_by_one(my_list[1:])


lll = [4, -3, 8]
print("Raise by one")
print(raise_by_one(lll))


def sum_of_threes(numb):
    if numb == 0:
        return 0
    if numb % 3 == 0 and numb % 2 == 0:
        return numb + sum_of_threes(numb - 1)
    else:
        return sum_of_threes(numb - 1)


print("Sum of threes")
print(sum_of_threes(9))


def in_list(my_list, x):
    if len(my_list) == 0:
        return False
    if my_list[0] == x:
        return True
    else:
        return in_list(my_list[1:], x)


print("In list")
print(in_list(lll, -3))


