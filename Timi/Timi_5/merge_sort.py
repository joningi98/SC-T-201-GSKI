def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i = i + 1
            else:
                my_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j = j + 1
            k = k + 1