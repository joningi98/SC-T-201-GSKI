

def the_sum_man(my_str):
    if len(my_str) == 1:
        return int(my_str)
    if len(my_str) > 1:
        return int(my_str[0]) + the_sum_man(my_str[1::])


print(the_sum_man("245"))

