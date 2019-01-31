

def sum_of_list(my_list):
    if len(my_list) == 1:
        return int(my_list[0])
    else:
        return int(my_list[0]) + int(sum_of_list(my_list[1::]))


the_list = [3, 6, 5]
print(sum_of_list(the_list))
