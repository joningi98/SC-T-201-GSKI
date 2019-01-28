
def length_of_string(my_str):
    if len(my_str) == 0:
        return 0
    else:
        return 1 + length_of_string(my_str[1:])


print(length_of_string("Hallo"))

