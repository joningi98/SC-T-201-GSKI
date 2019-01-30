def boner_search(my_list, value):
    mid = len(my_list) // 2
    if len(my_list) == 0:
        return False
    if value == my_list[mid]:
        return True
    elif value > mid:
        return boner_search(my_list[mid + 1:], value)
    elif value < mid:
        return boner_search(my_list[:mid], value)


the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(boner_search(the_list, 9))
