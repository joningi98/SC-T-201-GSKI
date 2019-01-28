def binary_search(my_list, target):
    mid = len(my_list) // 2
    if len(my_list) == 0:
        return False
    if target == my_list[mid]:
        return True
    elif target > my_list[mid]:
        return binary_search(my_list[mid + 1:], target)
    elif target < my_list[mid]:
        return binary_search(my_list[:mid], target)


the_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(the_list, 7))
