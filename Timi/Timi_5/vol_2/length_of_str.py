

def length(my_str):
    if len(my_str) == 1:
        return 1
    else:
        return 1 + len(my_str[1::])


print(length("hello"))
